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


from airflow import DAG
from airflow.providers.cncf.kubernetes.operators import kubernetes_pod
from airflow.providers.google.cloud.transfers import gcs_to_bigquery

default_args = {
    "owner": "Google",
    "depends_on_past": False,
    "start_date": "2022-09-01",
}


with DAG(
    dag_id="un_sdg.un_sdg",
    default_args=default_args,
    max_active_runs=1,
    schedule_interval="@daily",
    catchup=False,
    default_view="graph",
) as dag:

    # Run CSV transform within kubernetes pod
    un_sdg_transform_csv = kubernetes_pod.KubernetesPodOperator(
        task_id="un_sdg_transform_csv",
        name="un_sdg",
        namespace="composer",
        service_account_name="datasets",
        image_pull_policy="Always",
        image="{{ var.json.un_sdg.container_registry.run_csv_transform_kub }}",
        env_vars={
            "SOURCE_URL": '["gs://un_sdg/un_sdg_june_2018.csv"]',
            "SOURCE_FILE": '["files/data.csv"]',
            "TARGET_FILE": "files/data_output.csv",
            "TARGET_GCS_BUCKET": "{{ var.value.composer_bucket }}",
            "TARGET_GCS_PATH": "data/un_sdg/indicators/data_output.csv",
            "FILE_PATH": "files/",
            "CSV_HEADERS": '["goal",\n  "target",\n  "indicator",\n  "seriescode",\n  "seriesdescription",\n  "geoareacode",\n  "geoareaname",\n  "timeperiod",\n  "value",\n  "time_detail",\n  "source",\n  "footnote",\n  "nature",\n  "age",\n  "bounds",\n  "cities",\n  "education_level",\n  "freq",\n  "hazard_type",\n  "ihr_capacity",\n  "level_status",\n  "location",\n  "migratory_status",\n  "mode_of_transportation",\n  "name_of_international_institution",\n  "name_of_non_communicable_disease",\n  "sex",\n  "tariff_regime_status",\n  "type_of_mobile_technology",\n  "type_of_occupation",\n  "type_of_product",\n  "type_of_skill",\n  "type_of_speed",\n  "units"]',
            "RENAME_MAPPINGS": '{"Goal": "goal",\n  "Target": "target",\n  "Indicator": "indicator",\n  "SeriesCode": "seriescode",\n  "SeriesDescription": "seriesdescription",\n  "GeoAreaCode": "geoareacode",\n  "GeoAreaName": "geoareaname",\n  "TimePeriod": "timeperiod",\n  "Value": "value",\n  "Time_Detail": "time_detail",\n  "Source": "source",\n  "FootNote": "footnote",\n  "Nature": "nature",\n  "[Age]": "age",\n  "[Bounds]": "bounds",\n  "[Cities]": "cities",\n  "[Education level]": "education_level",\n  "[Freq]": "freq",\n  "[Hazard type]": "hazard_type",\n  "[IHR Capacity]": "ihr_capacity",\n  "[Level/Status]": "level_status",\n  "[Location]": "location",\n  "[Migratory status]": "migratory_status",\n  "[Mode of transportation]": "mode_of_transportation",\n  "[Name of international institution]": "name_of_international_institution",\n  "[Name of non-communicable disease]": "name_of_non_communicable_disease",\n  "[Sex]": "sex",\n  "[Tariff regime (status)]": "tariff_regime_status",\n  "[Type of mobile technology]": "type_of_mobile_technology",\n  "[Type of occupation]": "type_of_occupation",\n  "[Type of product]": "type_of_product",\n  "[Type of skill]": "type_of_skill",\n  "[Type of speed]": "type_of_speed",\n  "[Units]": "units"}',
        },
        resources={
            "request_memory": "4G",
            "request_cpu": "1",
            "request_ephemeral_storage": "10G",
        },
    )

    # Task to load CSV data to a BigQuery table
    load_un_sdg_data_to_bq = gcs_to_bigquery.GCSToBigQueryOperator(
        task_id="load_un_sdg_data_to_bq",
        bucket="{{ var.value.composer_bucket }}",
        source_objects=["data/un_sdg/indicators/data_output.csv"],
        source_format="CSV",
        destination_project_dataset_table="un_sdg.indicators",
        skip_leading_rows=1,
        allow_quoted_newlines=True,
        write_disposition="WRITE_TRUNCATE",
        schema_fields=[
            {
                "name": "goal",
                "mode": "NULLABLE",
                "type": "INTEGER",
                "description": "High-level goal for sustainable development",
            },
            {
                "name": "target",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Each goal has multiple targets. Specific data points that, when achieved, indicate substantial progress toward a goal",
            },
            {
                "name": "indicator",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Quantifiable metric used to determine progress towards reaching a target. Each target has between 1 and 3 indicators",
            },
            {
                "name": "seriescode",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Abbreviated string of characters for each specific indicator",
            },
            {
                "name": "seriesdescription",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Full text description of indicator",
            },
            {
                "name": "geoareacode",
                "mode": "NULLABLE",
                "type": "INTEGER",
                "description": "Numeric code of GeoArea",
            },
            {
                "name": "geoareaname",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Full text of GeoArea. Includes countries, regions, and continents",
            },
            {
                "name": "timeperiod",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Time period for which the value is relevant",
            },
            {
                "name": "value",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Numeric value of GeoArea",
            },
            {
                "name": "time_detail",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Time period in which the data was collected to calculate value",
            },
            {
                "name": "source",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Original source of data",
            },
            {
                "name": "footnote",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "Specific details regarding data for individual observation",
            },
            {"name": "nature", "mode": "NULLABLE", "type": "STRING", "description": ""},
            {"name": "age", "mode": "NULLABLE", "type": "STRING", "description": ""},
            {"name": "bounds", "mode": "NULLABLE", "type": "STRING", "description": ""},
            {"name": "cities", "mode": "NULLABLE", "type": "STRING", "description": ""},
            {
                "name": "education_level",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {"name": "freq", "mode": "NULLABLE", "type": "STRING", "description": ""},
            {
                "name": "hazard_type",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "ihr_capacity",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "level_status",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "location",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "migratory_status",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "mode_of_transportation",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "name_of_international_institution",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "name_of_non_communicable_disease",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {"name": "sex", "mode": "NULLABLE", "type": "STRING", "description": ""},
            {
                "name": "tariff_regime_status",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "type_of_mobile_technology",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "type_of_occupation",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "type_of_product",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "type_of_skill",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {
                "name": "type_of_speed",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "",
            },
            {"name": "units", "mode": "NULLABLE", "type": "STRING", "description": ""},
        ],
    )

    un_sdg_transform_csv >> load_un_sdg_data_to_bq
