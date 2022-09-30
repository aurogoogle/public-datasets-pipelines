# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import datetime
import glob
import json
import logging
import math
import os
import pathlib
import re
import subprocess
import typing

import pandas as pd
from google.cloud import storage


def main(
    source_url: typing.List[str],
    source_file: typing.List[pathlib.Path],
    source_files_path: str,
    target_file: pathlib.Path,
    target_gcs_bucket: str,
    target_gcs_path: str,
    headers: typing.List[str],
    rename_mappings: dict,
) -> None:

    logging.info(
        "un_sdg started at "
        + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )

    logging.info("Creating 'files' folder")
    pathlib.Path("./files").mkdir(parents=True, exist_ok=True)

    logging.info("Downloading file ...")
    download_file(source_url, source_file)

    logging.info("Opening files...")
    df = read_files(source_files_path)

    logging.info("Transform: Rename columns...")
    rename_headers(df, rename_mappings)

    logging.info("Transform: Replacing values...")
    df["footnote"] = df["footnote"].apply(lambda x: "-" if str(x) == "nan" else str(x))
    df["footnote"] = df["footnote"].apply(reg_exp_tranformation, args=(r"\n", " "))
    df["source"] = df["source"].apply(lambda x: "-" if str(x) == "nan" else str(x))
    df["source"] = df["source"].apply(reg_exp_tranformation, args=(r"\n", " "))
    df["seriesdescription"] = df["seriesdescription"].apply(lambda x: "-" if str(x) == "nan" else str(x))
    df["seriesdescription"] = df["seriesdescription"].apply(reg_exp_tranformation, args=(r"\n", " "))

    logging.info("Transform: Converting to integer string...")
    df["target"] = df["target"].apply(lambda x: str(x))
    df["units"] = df["units"].apply(lambda x: str(x))
    df["type_of_speed"] = df["type_of_speed"].apply(lambda x: str(x))

    logging.info("Transform: Reordering headers...")
    df = df[headers]

    logging.info(f"Saving to output file.. {target_file}")
    try:
        save_to_new_file(df, file_path=str(target_file))
    except Exception as e:
        logging.error(f"Error saving output file: {e}.")

    logging.info(
        f"Uploading output file to.. gs://{target_gcs_bucket}/{target_gcs_path}"
    )
    upload_file_to_gcs(target_file, target_gcs_bucket, target_gcs_path)

    logging.info(
        "un_sdg completed at "
        + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )


def download_file(
    source_url: typing.List[str], source_file: typing.List[pathlib.Path]
) -> None:
    for url, file in zip(source_url, source_file):
        logging.info(f"Downloading file from {url} ...")
        subprocess.check_call(["gsutil", "cp", f"{url}", f"{file}"])


def read_files(path: pathlib.Path) -> pd.DataFrame:
    all_files = glob.glob(path + "/*.csv")
    df_temp = []
    for filename in all_files:
        frame = pd.read_csv(filename, index_col=None, header=0)
        df_temp.append(frame)
    df = pd.concat(df_temp, axis=0, ignore_index=True)
    return df


def rename_headers(df: pd.DataFrame, rename_mappings: dict) -> None:
    df.rename(columns=rename_mappings, inplace=True)


def reg_exp_tranformation(str_value: str, search_pattern: str, replace_val: str) -> str:
    str_value = re.sub(search_pattern, replace_val, str_value)
    return str_value


def convert_to_integer_string(input: typing.Union[str, float]) -> str:
    str_val = ""
    if not input or (math.isnan(input)):
        str_val = ""
    else:
        str_val = str(int(round(input, 0)))
    return str_val


def convert_dt_format(dt_str: str) -> str:
    a = ""
    if not dt_str or str(dt_str) == "nan":
        return str(a)
    else:
        return datetime.datetime.strptime(str(dt_str), "%m/%d/%Y %H:%M:%S %p").strftime(
            "%Y-%m-%d %H:%M:%S"
        )


def extract_year(string_val: str) -> str:
    string_val = string_val[0:4]
    return string_val


def convert_exp_to_float(exp_val: str) -> str:
    float_val = "{:f}".format(float(exp_val))
    return float_val


def search_string(str_value: str) -> str:
    if re.search(r".*\(.*\)", str_value):
        return str(str_value)
    else:
        return str("")


def extract_lat_long(str_val: str, patter: str) -> str:
    m = re.match(patter, str_val)
    if m:
        return m.group(1)
    else:
        return ""


def delete_column(df: pd.DataFrame, column_name: str) -> None:
    df = df.drop(column_name, axis=1, inplace=True)


def upload_file_to_gcs(file_path: pathlib.Path, gcs_bucket: str, gcs_path: str) -> None:
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket)
    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(file_path)


def save_to_new_file(df: pd.DataFrame, file_path: str) -> None:
    df.to_csv(file_path, index=False)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main(
        source_url=json.loads(os.environ["SOURCE_URL"]),
        source_file=json.loads(os.environ["SOURCE_FILE"]),
        source_files_path=os.environ["FILE_PATH"],
        target_file=pathlib.Path(os.environ["TARGET_FILE"]).expanduser(),
        target_gcs_bucket=os.environ["TARGET_GCS_BUCKET"],
        target_gcs_path=os.environ["TARGET_GCS_PATH"],
        headers=json.loads(os.environ["CSV_HEADERS"]),
        rename_mappings=json.loads(os.environ["RENAME_MAPPINGS"]),
    )
