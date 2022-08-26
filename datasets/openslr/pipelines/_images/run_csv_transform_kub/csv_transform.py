# Copyright 2022 Google LLC
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
import json
import logging
import os
import pathlib

import requests
from google.cloud import exceptions, storage


def main(
    pipeline_name: str,
    target_gcs_bucket: str,
    meta_data_path: str,
) -> None:
    logging.info(
        f"ML datasets {pipeline_name} process started at "
        + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    execute_pipeline( target_gcs_bucket=target_gcs_bucket,
    meta_data_path=meta_data_path)
    logging.info(
        f"ML datasets {pipeline_name} process completed at "
        + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )


def execute_pipeline (
    target_gcs_bucket: str,
    meta_data_path: str,
    ) -> None:
    try:
        bucket_name=target_gcs_bucket
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(meta_data_path)
        openslr_resource_struct = json.loads(blob.download_as_string(client=None))
        for info in openslr_resource_struct:
            new_folder_id = info["Resource"]
            new_folder_name = info["Name"]
            new_folder_category = info["Category"]
            new_folder_summary = info["Summary"]
            new_folder_download_list = info["Downloads"]
            logging.info(f"Creating 'Openslr folders'-> {new_folder_id} folder")
            folder_path = f"./Openslr_files/{new_folder_id}/"
            pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
            for source_url in new_folder_download_list:
                download_file_name = source_url.rsplit('/',-1)[-1]
                source_file = f"Openslr_files/{new_folder_id}/{download_file_name}"
                download_file(source_url, source_file)
                target_file=source_file
                target_gcs_bucket=bucket_name
                target_gcs_path=f"data/openslr/openslr/{new_folder_id}/{download_file_name}"
                upload_file_to_gcs(target_file, target_gcs_bucket, target_gcs_path)
    except exceptions.NotFound:
        logging.info(f"Sorry, that bucket {bucket} does not exist!")


def download_file(source_url: str, source_file: pathlib.Path) -> None:
    logging.info(f"Downloading {source_url} into {source_file}")
    r = requests.get(source_url, stream=True)
    if r.status_code == 200:
        with open(source_file, "wb") as f:
            for chunk in r:
                f.write(chunk)
    else:
        logging.error(f"Couldn't download {source_url}: {r.text}")


def upload_file_to_gcs(
    file_path: pathlib.Path, target_gcs_bucket: str, target_gcs_path: str
) -> None:
    if os.path.exists(file_path):
        logging.info(
            f"Uploading output file to gs://{target_gcs_bucket}/{target_gcs_path}"
        )
        storage_client = storage.Client()
        bucket = storage_client.bucket(target_gcs_bucket)
        blob = bucket.blob(target_gcs_path)
        blob.upload_from_filename(file_path)
    else:
        logging.info(
            f"Cannot upload file to gs://{target_gcs_bucket}/{target_gcs_path} as it does not exist."
        )


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main(
        pipeline_name=os.environ["PIPELINE_NAME"],
        target_gcs_bucket=os.environ["TARGET_GCS_BUCKET"],
        meta_data_path=os.environ["META_DATA_PATH"]
    )
