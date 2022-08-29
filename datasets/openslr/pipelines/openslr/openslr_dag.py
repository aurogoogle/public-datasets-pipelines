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
from airflow.operators import bash

default_args = {
    "owner": "Google",
    "depends_on_past": False,
    "start_date": "2022-06-10",
}


with DAG(
    dag_id="openslr.openslr",
    default_args=default_args,
    max_active_runs=1,
    schedule_interval="@monthly",
    catchup=False,
    default_view="graph",
) as dag:

    # create folders for uploading openslr data to GCS
    create_folder = bash.BashOperator(
        task_id="create_folder",
        bash_command="mkdir -p $data_dir/openslr\ndeclare -a folder_name_array=(\u0027SLR1\tSLR2\tSLR3\tSLR4\tSLR5\tSLR6\tSLR7\tSLR8\tSLR9\tSLR10\tSLR11\tSLR12\tSLR13\tSLR14\tSLR15\tSLR16\tSLR17\tSLR18\tSLR19\tSLR20\tSLR21\tSLR22\tSLR23\tSLR24\tSLR25\tSLR26\tSLR27\tSLR28\tSLR29\tSLR30\tSLR31\tSLR32\tSLR33\tSLR34\tSLR35\tSLR36\tSLR37\tSLR38\tSLR39\tSLR40\tSLR41\tSLR42\tSLR43\tSLR44\tSLR45\tSLR46\tSLR47\tSLR48\tSLR49\tSLR50\tSLR51\tSLR52\tSLR53\tSLR54\tSLR55\tSLR56\tSLR57\tSLR58\tSLR59\tSLR60\tSLR61\tSLR62\tSLR63\tSLR64\tSLR65\tSLR66\tSLR67\tSLR68\tSLR69\tSLR70\tSLR71\tSLR72\tSLR73\tSLR74\tSLR75\tSLR76\tSLR77\tSLR78\tSLR79\tSLR80\tSLR81\tSLR82\tSLR83\tSLR84\tSLR85\tSLR86\tSLR87\tSLR88\tSLR89\tSLR92\tSLR93\tSLR94\tSLR95\tSLR96\tSLR97\tSLR98\tSLR99\tSLR100\tSLR101\tSLR102\tSLR103\tSLR104\tSLR105\tSLR106\tSLR107\tSLR108\tSLR109\tSLR110\tSLR111\tSLR112\tSLR113\tSLR114\tSLR115\tSLR116\tSLR117\tSLR118\tSLR119\tSLR120\tSLR122\tSLR123\tSLR124\tSLR125\tSLR126\tSLR127\tSLR128\tSLR129\u0027)\nfor val in ${folder_name_array[*]};\ndo\n  mkdir -p $data_dir/openslr/$val\ndone\n",
        env={"data_dir": "/home/airflow/gcs/data/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch1 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch1",
        bash_command="wget https://www.openslr.org/resources/1/waves_yesno.tar.gz -O $openslr_data_dir/SLR1/waves_yesno.tar.gz\nwget https://www.openslr.org/resources/2/openfst-1.3.2.tar.gz -O $openslr_data_dir/SLR2/openfst-1.3.2.tar.gz\nwget https://www.openslr.org/resources/2/openfst-1.3.3.tar.gz -O $openslr_data_dir/SLR2/openfst-1.3.3.tar.gz\nwget https://www.openslr.org/resources/2/openfst-1.3.4.tar.gz -O $openslr_data_dir/SLR2/openfst-1.3.4.tar.gz\nwget https://www.openslr.org/resources/2/openfst-1.4.1.tar.gz -O $openslr_data_dir/SLR2/openfst-1.4.1.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch2 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch2",
        bash_command="wget https://www.openslr.org/resources/2/openfst-1.5.4.tar.gz -O $openslr_data_dir/SLR2/openfst-1.5.4.tar.gz\nwget https://www.openslr.org/resources/2/openfst-1.6.2.tar.gz -O $openslr_data_dir/SLR2/openfst-1.6.2.tar.gz\nwget https://www.openslr.org/resources/2/openfst-1.6.5.tar.gz -O $openslr_data_dir/SLR2/openfst-1.6.5.tar.gz\nwget https://www.openslr.org/resources/2/openfst-1.6.7.tar.gz -O $openslr_data_dir/SLR2/openfst-1.6.7.tar.gz\nwget https://www.openslr.org/resources/2/openfst-1.7.2.tar.gz -O $openslr_data_dir/SLR2/openfst-1.7.2.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch3 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch3",
        bash_command="wget https://www.openslr.org/resources/2/openfst-1.7.9.tar.gz -O $openslr_data_dir/SLR2/openfst-1.7.9.tar.gz\nwget https://www.openslr.org/resources/3/sph2pipe_v2.5.tar.gz -O $openslr_data_dir/SLR3/sph2pipe_v2.5.tar.gz\nwget https://www.openslr.org/resources/4/sctk-2.4.0-20091110-0958.tar.bz2 -O $openslr_data_dir/SLR4/sctk-2.4.0-20091110-0958.tar.bz2\nwget https://www.openslr.org/resources/4/sctk-2.4.0-20091110-0958.tar.gz -O $openslr_data_dir/SLR4/sctk-2.4.0-20091110-0958.tar.gz\nwget https://www.openslr.org/resources/4/sctk-2.4.8-20130429-2145.tar.bz2 -O $openslr_data_dir/SLR4/sctk-2.4.8-20130429-2145.tar.bz2\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch4 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch4",
        bash_command="wget https://www.openslr.org/resources/4/sctk-2.4.9-20141015-1634Z.tar.bz2 -O $openslr_data_dir/SLR4/sctk-2.4.9-20141015-1634Z.tar.bz2\nwget https://www.openslr.org/resources/4/sctk-2.4.10-20151007-1312Z.tar.bz2 -O $openslr_data_dir/SLR4/sctk-2.4.10-20151007-1312Z.tar.bz2\nwget https://www.openslr.org/resources/5/switchboard_word_alignments.tar.gz -O $openslr_data_dir/SLR5/switchboard_word_alignments.tar.gz\nwget https://www.openslr.org/resources/5/sw-ms98-dict.text -O $openslr_data_dir/SLR5/sw-ms98-dict.text\nwget https://www.openslr.org/resources/6/data_voip_cs.tgz -O $openslr_data_dir/SLR6/data_voip_cs.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch5 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch5",
        bash_command="wget https://www.openslr.org/resources/6/data_voip_en.tgz -O $openslr_data_dir/SLR6/data_voip_en.tgz\nwget https://www.openslr.org/resources/7/TEDLIUM_release1.tar.gz -O $openslr_data_dir/SLR7/TEDLIUM_release1.tar.gz\nwget https://www.openslr.org/resources/8/lexicon-da.tgz -O $openslr_data_dir/SLR8/lexicon-da.tgz\nwget https://www.openslr.org/resources/8/lexicon-da-nonorm.tgz -O $openslr_data_dir/SLR8/lexicon-da-nonorm.tgz\nwget https://www.openslr.org/resources/9/wordlist.50k.gz -O $openslr_data_dir/SLR9/wordlist.50k.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch6 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch6",
        bash_command="wget https://www.openslr.org/resources/10/sre2000-key.tar.gz -O $openslr_data_dir/SLR10/sre2000-key.tar.gz\nwget https://www.openslr.org/resources/10/sre04_key.tgz -O $openslr_data_dir/SLR10/sre04_key.tgz\nwget https://www.openslr.org/resources/10/sre04_key-v2.txt.gz -O $openslr_data_dir/SLR10/sre04_key-v2.txt.gz\nwget https://www.openslr.org/resources/10/sre05-key-v7b.txt.gz -O $openslr_data_dir/SLR10/sre05-key-v7b.txt.gz\nwget https://www.openslr.org/resources/11/librispeech-lm-corpus.tgz -O $openslr_data_dir/SLR11/librispeech-lm-corpus.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch7 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch7",
        bash_command="wget https://www.openslr.org/resources/11/librispeech-lm-norm.txt.gz -O $openslr_data_dir/SLR11/librispeech-lm-norm.txt.gz\nwget https://www.openslr.org/resources/11/librispeech-vocab.txt -O $openslr_data_dir/SLR11/librispeech-vocab.txt\nwget https://www.openslr.org/resources/11/librispeech-lexicon.txt -O $openslr_data_dir/SLR11/librispeech-lexicon.txt\nwget https://www.openslr.org/resources/11/3-gram.arpa.gz -O $openslr_data_dir/SLR11/3-gram.arpa.gz\nwget https://www.openslr.org/resources/11/3-gram.pruned.1e-7.arpa.gz -O $openslr_data_dir/SLR11/3-gram.pruned.1e-7.arpa.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch8 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch8",
        bash_command="wget https://www.openslr.org/resources/11/3-gram.pruned.3e-7.arpa.gz -O $openslr_data_dir/SLR11/3-gram.pruned.3e-7.arpa.gz\nwget https://www.openslr.org/resources/11/4-gram.arpa.gz -O $openslr_data_dir/SLR11/4-gram.arpa.gz\nwget https://www.openslr.org/resources/11/g2p-model-5 -O $openslr_data_dir/SLR11/g2p-model-5\nwget https://www.openslr.org/resources/12/dev-clean.tar.gz -O $openslr_data_dir/SLR12/dev-clean.tar.gz\nwget https://www.openslr.org/resources/12/dev-other.tar.gz -O $openslr_data_dir/SLR12/dev-other.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch9 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch9",
        bash_command="wget https://www.openslr.org/resources/12/test-clean.tar.gz -O $openslr_data_dir/SLR12/test-clean.tar.gz\nwget https://www.openslr.org/resources/12/test-other.tar.gz -O $openslr_data_dir/SLR12/test-other.tar.gz\nwget https://www.openslr.org/resources/12/train-clean-100.tar.gz -O $openslr_data_dir/SLR12/train-clean-100.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch10 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch10",
        bash_command="wget https://www.openslr.org/resources/12/train-clean-360.tar.gz -O $openslr_data_dir/SLR12/train-clean-360.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch11 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch11",
        bash_command="wget https://www.openslr.org/resources/12/train-other-500.tar.gz -O $openslr_data_dir/SLR12/train-other-500.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch12 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch12",
        bash_command="wget https://www.openslr.org/resources/12/intro-disclaimers.tar.gz -O $openslr_data_dir/SLR12/intro-disclaimers.tar.gz\nwget https://www.openslr.org/resources/12/original-books.tar.gz -O $openslr_data_dir/SLR12/original-books.tar.gz\nwget https://www.openslr.org/resources/12/raw-metadata.tar.gz -O $openslr_data_dir/SLR12/raw-metadata.tar.gz\nwget https://www.openslr.org/resources/12/md5sum.txt -O $openslr_data_dir/SLR12/md5sum.txt\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch13 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch13",
        bash_command="wget https://www.openslr.org/resources/13/RWCP.tar.gz -O $openslr_data_dir/SLR13/RWCP.tar.gz\nwget https://www.openslr.org/resources/14/beep.tar.gz -O $openslr_data_dir/SLR14/beep.tar.gz\nwget https://www.openslr.org/resources/15/speaker_list.tgz -O $openslr_data_dir/SLR15/speaker_list.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch14 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch14",
        bash_command="wget https://www.openslr.org/resources/16/ami_manual_1.6.1.tar.gz -O $openslr_data_dir/SLR16/ami_manual_1.6.1.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch15 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch15",
        bash_command="wget https://www.openslr.org/resources/16/headset.tar.gz -O $openslr_data_dir/SLR16/headset.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch16 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch16",
        bash_command="wget https://www.openslr.org/resources/16/Array1-01.tar.gz -O $openslr_data_dir/SLR16/Array1-01.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch17 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch17",
        bash_command="wget https://www.openslr.org/resources/16/Array1-02.tar.gz -O $openslr_data_dir/SLR16/Array1-02.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch18 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch18",
        bash_command="wget https://www.openslr.org/resources/16/Array1-03.tar.gz -O $openslr_data_dir/SLR16/Array1-03.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch19 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch19",
        bash_command="wget https://www.openslr.org/resources/16/Array1-04.tar.gz -O $openslr_data_dir/SLR16/Array1-04.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch20 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch20",
        bash_command="wget https://www.openslr.org/resources/16/Array1-05.tar.gz -O $openslr_data_dir/SLR16/Array1-05.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch21 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch21",
        bash_command="wget https://www.openslr.org/resources/16/Array1-06.tar.gz -O $openslr_data_dir/SLR16/Array1-06.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch22 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch22",
        bash_command="wget https://www.openslr.org/resources/16/Array1-07.tar.gz -O $openslr_data_dir/SLR16/Array1-07.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch23 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch23",
        bash_command="wget https://www.openslr.org/resources/16/Array1-08.tar.gz -O $openslr_data_dir/SLR16/Array1-08.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch24 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch24",
        bash_command="wget https://www.openslr.org/resources/17/musan.tar.gz -O $openslr_data_dir/SLR17/musan.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch25 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch25",
        bash_command="wget https://www.openslr.org/resources/18/test-noise.tgz -O $openslr_data_dir/SLR18/test-noise.tgz\nwget https://www.openslr.org/resources/18/resource.tgz -O $openslr_data_dir/SLR18/resource.tgz\nwget https://www.openslr.org/resources/18/data_thchs30.tgz -O $openslr_data_dir/SLR18/data_thchs30.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch26 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch26",
        bash_command="wget https://www.openslr.org/resources/19/TEDLIUM_release2.tar.gz -O $openslr_data_dir/SLR19/TEDLIUM_release2.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch27 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch27",
        bash_command="wget https://www.openslr.org/resources/20/air_database_release_1_4.zip -O $openslr_data_dir/SLR20/air_database_release_1_4.zip\nwget https://www.openslr.org/resources/21/es_wordlist.json.tgz -O $openslr_data_dir/SLR21/es_wordlist.json.tgz\nwget https://www.openslr.org/resources/22/data_thuyg20.tar.gz -O $openslr_data_dir/SLR22/data_thuyg20.tar.gz\nwget https://www.openslr.org/resources/22/data_thuyg20_sre.tar.gz -O $openslr_data_dir/SLR22/data_thuyg20_sre.tar.gz\nwget https://www.openslr.org/resources/22/test_noise.tar.gz -O $openslr_data_dir/SLR22/test_noise.tar.gz\nwget https://www.openslr.org/resources/22/test_noise_sre.tar.gz -O $openslr_data_dir/SLR22/test_noise_sre.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch28 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch28",
        bash_command="wget https://www.openslr.org/resources/22/resource.tar.gz -O $openslr_data_dir/SLR22/resource.tar.gz\nwget https://www.openslr.org/resources/23/lre07_key.txt -O $openslr_data_dir/SLR23/lre07_key.txt\nwget https://www.openslr.org/resources/24/iban.tar.gz -O $openslr_data_dir/SLR24/iban.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch29 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch29",
        bash_command="wget https://www.openslr.org/resources/25/data_readspeech_am.tar.bz2 -O $openslr_data_dir/SLR25/data_readspeech_am.tar.bz2\nwget https://www.openslr.org/resources/25/data_broadcastnews_sw.tar.bz2 -O $openslr_data_dir/SLR25/data_broadcastnews_sw.tar.bz2\nwget https://www.openslr.org/resources/25/data_readspeech_wo.tar.bz2 -O $openslr_data_dir/SLR25/data_readspeech_wo.tar.bz2\nwget https://www.openslr.org/resources/26/sim_rir_8k.zip -O $openslr_data_dir/SLR26/sim_rir_8k.zip\nwget https://www.openslr.org/resources/26/sim_rir_16k.zip -O $openslr_data_dir/SLR26/sim_rir_16k.zip\nwget https://www.openslr.org/resources/27/cantab-TEDLIUM.tar.bz2 -O $openslr_data_dir/SLR27/cantab-TEDLIUM.tar.bz2\nwget https://www.openslr.org/resources/27/cantab-TEDLIUM-partial.tar.bz2 -O $openslr_data_dir/SLR27/cantab-TEDLIUM-partial.tar.bz2\nwget https://www.openslr.org/resources/28/rirs_noises.zip -O $openslr_data_dir/SLR28/rirs_noises.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch30 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch30",
        bash_command="wget https://www.openslr.org/resources/29/lexicon-sv.tgz -O $openslr_data_dir/SLR29/lexicon-sv.tgz\nwget https://www.openslr.org/resources/30/si_lk.tar.gz -O $openslr_data_dir/SLR30/si_lk.tar.gz\nwget https://www.openslr.org/resources/30/si_lk.lines.txt -O $openslr_data_dir/SLR30/si_lk.lines.txt\nwget https://www.openslr.org/resources/30/README.txt -O $openslr_data_dir/SLR30/README.txt\nwget https://www.openslr.org/resources/30/LICENSE.txt -O $openslr_data_dir/SLR30/LICENSE.txt\nwget https://www.openslr.org/resources/31/dev-clean-2.tar.gz -O $openslr_data_dir/SLR31/dev-clean-2.tar.gz\nwget https://www.openslr.org/resources/31/train-clean-5.tar.gz -O $openslr_data_dir/SLR31/train-clean-5.tar.gz\nwget https://www.openslr.org/resources/31/md5sum.txt -O $openslr_data_dir/SLR31/md5sum.txt\nwget https://www.openslr.org/resources/32/af_za.tar.gz -O $openslr_data_dir/SLR32/af_za.tar.gz\nwget https://www.openslr.org/resources/32/st_za.tar.gz -O $openslr_data_dir/SLR32/st_za.tar.gz\nwget https://www.openslr.org/resources/32/tn_za.tar.gz -O $openslr_data_dir/SLR32/tn_za.tar.gz\nwget https://www.openslr.org/resources/32/xh_za.tar.gz -O $openslr_data_dir/SLR32/xh_za.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch31 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch31",
        bash_command="wget https://www.openslr.org/resources/33/data_aishell.tgz -O $openslr_data_dir/SLR33/data_aishell.tgz\nwget https://www.openslr.org/resources/33/resource_aishell.tgz -O $openslr_data_dir/SLR33/resource_aishell.tgz\nwget https://www.openslr.org/resources/34/santiago.tar.gz -O $openslr_data_dir/SLR34/santiago.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch32 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch32",
        bash_command="wget https://www.openslr.org/resources/35/asr_javanese.sha256 -O $openslr_data_dir/SLR35/asr_javanese.sha256\nwget https://www.openslr.org/resources/35/LICENSE -O $openslr_data_dir/SLR35/LICENSE\nwget https://www.openslr.org/resources/35/utt_spk_text.tsv -O $openslr_data_dir/SLR35/utt_spk_text.tsv\nwget https://www.openslr.org/resources/35/asr_javanese_0.zip -O $openslr_data_dir/SLR35/asr_javanese_0.zip\nwget https://www.openslr.org/resources/35/asr_javanese_1.zip -O $openslr_data_dir/SLR35/asr_javanese_1.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch33 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch33",
        bash_command="wget https://www.openslr.org/resources/35/asr_javanese_2.zip -O $openslr_data_dir/SLR35/asr_javanese_2.zip\nwget https://www.openslr.org/resources/35/asr_javanese_3.zip -O $openslr_data_dir/SLR35/asr_javanese_3.zip\nwget https://www.openslr.org/resources/35/asr_javanese_4.zip -O $openslr_data_dir/SLR35/asr_javanese_4.zip\nwget https://www.openslr.org/resources/35/asr_javanese_5.zip -O $openslr_data_dir/SLR35/asr_javanese_5.zip\nwget https://www.openslr.org/resources/35/asr_javanese_6.zip -O $openslr_data_dir/SLR35/asr_javanese_6.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch34 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch34",
        bash_command="wget https://www.openslr.org/resources/35/asr_javanese_7.zip -O $openslr_data_dir/SLR35/asr_javanese_7.zip\nwget https://www.openslr.org/resources/35/asr_javanese_8.zip -O $openslr_data_dir/SLR35/asr_javanese_8.zip\nwget https://www.openslr.org/resources/35/asr_javanese_9.zip -O $openslr_data_dir/SLR35/asr_javanese_9.zip\nwget https://www.openslr.org/resources/35/asr_javanese_a.zip -O $openslr_data_dir/SLR35/asr_javanese_a.zip\nwget https://www.openslr.org/resources/35/asr_javanese_b.zip -O $openslr_data_dir/SLR35/asr_javanese_b.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch35 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch35",
        bash_command="wget https://www.openslr.org/resources/35/asr_javanese_c.zip -O $openslr_data_dir/SLR35/asr_javanese_c.zip\nwget https://www.openslr.org/resources/35/asr_javanese_d.zip -O $openslr_data_dir/SLR35/asr_javanese_d.zip\nwget https://www.openslr.org/resources/35/asr_javanese_e.zip -O $openslr_data_dir/SLR35/asr_javanese_e.zip\nwget https://www.openslr.org/resources/35/asr_javanese_f.zip -O $openslr_data_dir/SLR35/asr_javanese_f.zip\nwget https://www.openslr.org/resources/36/asr_sundanese.sha256 -O $openslr_data_dir/SLR36/asr_sundanese.sha256\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch36 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch36",
        bash_command="wget https://www.openslr.org/resources/36/LICENSE -O $openslr_data_dir/SLR36/LICENSE\nwget https://www.openslr.org/resources/36/utt_spk_text.tsv -O $openslr_data_dir/SLR36/utt_spk_text.tsv\nwget https://www.openslr.org/resources/36/asr_sundanese_0.zip -O $openslr_data_dir/SLR36/asr_sundanese_0.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_1.zip -O $openslr_data_dir/SLR36/asr_sundanese_1.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_2.zip -O $openslr_data_dir/SLR36/asr_sundanese_2.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch37 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch37",
        bash_command="wget https://www.openslr.org/resources/36/asr_sundanese_3.zip -O $openslr_data_dir/SLR36/asr_sundanese_3.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_4.zip -O $openslr_data_dir/SLR36/asr_sundanese_4.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_5.zip -O $openslr_data_dir/SLR36/asr_sundanese_5.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_6.zip -O $openslr_data_dir/SLR36/asr_sundanese_6.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_7.zip -O $openslr_data_dir/SLR36/asr_sundanese_7.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch38 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch38",
        bash_command="wget https://www.openslr.org/resources/36/asr_sundanese_8.zip -O $openslr_data_dir/SLR36/asr_sundanese_8.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_9.zip -O $openslr_data_dir/SLR36/asr_sundanese_9.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_a.zip -O $openslr_data_dir/SLR36/asr_sundanese_a.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_b.zip -O $openslr_data_dir/SLR36/asr_sundanese_b.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_c.zip -O $openslr_data_dir/SLR36/asr_sundanese_c.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch39 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch39",
        bash_command="wget https://www.openslr.org/resources/36/asr_sundanese_d.zip -O $openslr_data_dir/SLR36/asr_sundanese_d.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_e.zip -O $openslr_data_dir/SLR36/asr_sundanese_e.zip\nwget https://www.openslr.org/resources/36/asr_sundanese_f.zip -O $openslr_data_dir/SLR36/asr_sundanese_f.zip\nwget https://www.openslr.org/resources/37/bn_bd.zip -O $openslr_data_dir/SLR37/bn_bd.zip\nwget https://www.openslr.org/resources/37/bn_in.zip -O $openslr_data_dir/SLR37/bn_in.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch40 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch40",
        bash_command="wget https://www.openslr.org/resources/37/README.txt -O $openslr_data_dir/SLR37/README.txt\nwget https://www.openslr.org/resources/37/LICENSE.txt -O $openslr_data_dir/SLR37/LICENSE.txt\nwget https://www.openslr.org/resources/38/ST-CMDS-20170001_1-OS.tar.gz -O $openslr_data_dir/SLR38/ST-CMDS-20170001_1-OS.tar.gz\nwget https://www.openslr.org/resources/39/LDC2006S37.tar.gz -O $openslr_data_dir/SLR39/LDC2006S37.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch41 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch41",
        bash_command="wget https://www.openslr.org/resources/40/zeroth_korean.tar.gz -O $openslr_data_dir/SLR40/zeroth_korean.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch42 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch42",
        bash_command="wget https://www.openslr.org/resources/41/jv_id_female.zip -O $openslr_data_dir/SLR41/jv_id_female.zip\nwget https://www.openslr.org/resources/41/jv_id_male.zip -O $openslr_data_dir/SLR41/jv_id_male.zip\nwget https://www.openslr.org/resources/41/LICENSE -O $openslr_data_dir/SLR41/LICENSE\nwget https://www.openslr.org/resources/42/km_kh_male.zip -O $openslr_data_dir/SLR42/km_kh_male.zip\nwget https://www.openslr.org/resources/42/LICENSE -O $openslr_data_dir/SLR42/LICENSE\nwget https://www.openslr.org/resources/43/ne_np_female.zip -O $openslr_data_dir/SLR43/ne_np_female.zip\nwget https://www.openslr.org/resources/43/LICENSE -O $openslr_data_dir/SLR43/LICENSE\nwget https://www.openslr.org/resources/44/su_id_female.zip -O $openslr_data_dir/SLR44/su_id_female.zip\nwget https://www.openslr.org/resources/44/su_id_male.zip -O $openslr_data_dir/SLR44/su_id_male.zip\nwget https://www.openslr.org/resources/44/LICENSE -O $openslr_data_dir/SLR44/LICENSE\nwget https://www.openslr.org/resources/45/ST-AEDS-20180100_1-OS.tgz -O $openslr_data_dir/SLR45/ST-AEDS-20180100_1-OS.tgz\nwget https://www.openslr.org/resources/46/Tunisian_MSA.tar.gz -O $openslr_data_dir/SLR46/Tunisian_MSA.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch43 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch43",
        bash_command="wget https://www.openslr.org/resources/47/primewords_md_2018_set1.tar.gz -O $openslr_data_dir/SLR47/primewords_md_2018_set1.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch44 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch44",
        bash_command="wget https://www.openslr.org/resources/48/madcat.dev.raw.lineid -O $openslr_data_dir/SLR48/madcat.dev.raw.lineid\nwget https://www.openslr.org/resources/48/madcat.test.raw.lineid -O $openslr_data_dir/SLR48/madcat.test.raw.lineid\nwget https://www.openslr.org/resources/48/madcat.train.raw.lineid -O $openslr_data_dir/SLR48/madcat.train.raw.lineid\nwget https://www.openslr.org/resources/49/voxceleb1_test.txt -O $openslr_data_dir/SLR49/voxceleb1_test.txt\nwget https://www.openslr.org/resources/49/voxceleb1_test_v2.txt -O $openslr_data_dir/SLR49/voxceleb1_test_v2.txt\nwget https://www.openslr.org/resources/49/voxceleb1_sitw_overlap.txt -O $openslr_data_dir/SLR49/voxceleb1_sitw_overlap.txt\nwget https://www.openslr.org/resources/49/vox1_meta.csv -O $openslr_data_dir/SLR49/vox1_meta.csv\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch45 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch45",
        bash_command="wget https://www.openslr.org/resources/49/vox2_meta.csv -O $openslr_data_dir/SLR49/vox2_meta.csv\nwget https://www.openslr.org/resources/50/madcat.dev.raw.lineid -O $openslr_data_dir/SLR50/madcat.dev.raw.lineid\nwget https://www.openslr.org/resources/50/madcat.test.raw.lineid -O $openslr_data_dir/SLR50/madcat.test.raw.lineid\nwget https://www.openslr.org/resources/50/madcat.train.raw.lineid -O $openslr_data_dir/SLR50/madcat.train.raw.lineid\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch46 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch46",
        bash_command="wget https://www.openslr.org/resources/52/about.html -O $openslr_data_dir/SLR52/about.html\nwget https://www.openslr.org/resources/52/LICENSE -O $openslr_data_dir/SLR52/LICENSE\nwget https://www.openslr.org/resources/52/utt_spk_text.tsv -O $openslr_data_dir/SLR52/utt_spk_text.tsv\nwget https://www.openslr.org/resources/52/asr_sinhala_0.zip -O $openslr_data_dir/SLR52/asr_sinhala_0.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_1.zip -O $openslr_data_dir/SLR52/asr_sinhala_1.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch47 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch47",
        bash_command="wget https://www.openslr.org/resources/52/asr_sinhala_2.zip -O $openslr_data_dir/SLR52/asr_sinhala_2.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_3.zip -O $openslr_data_dir/SLR52/asr_sinhala_3.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_4.zip -O $openslr_data_dir/SLR52/asr_sinhala_4.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_5.zip -O $openslr_data_dir/SLR52/asr_sinhala_5.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_6.zip -O $openslr_data_dir/SLR52/asr_sinhala_6.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch48 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch48",
        bash_command="wget https://www.openslr.org/resources/52/asr_sinhala_7.zip -O $openslr_data_dir/SLR52/asr_sinhala_7.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_8.zip -O $openslr_data_dir/SLR52/asr_sinhala_8.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_9.zip -O $openslr_data_dir/SLR52/asr_sinhala_9.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_a.zip -O $openslr_data_dir/SLR52/asr_sinhala_a.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_b.zip -O $openslr_data_dir/SLR52/asr_sinhala_b.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch49 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch49",
        bash_command="wget https://www.openslr.org/resources/52/asr_sinhala_c.zip -O $openslr_data_dir/SLR52/asr_sinhala_c.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_d.zip -O $openslr_data_dir/SLR52/asr_sinhala_d.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_e.zip -O $openslr_data_dir/SLR52/asr_sinhala_e.zip\nwget https://www.openslr.org/resources/52/asr_sinhala_f.zip -O $openslr_data_dir/SLR52/asr_sinhala_f.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch50 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch50",
        bash_command="wget https://www.openslr.org/resources/53/about.html -O $openslr_data_dir/SLR53/about.html\nwget https://www.openslr.org/resources/53/LICENSE -O $openslr_data_dir/SLR53/LICENSE\nwget https://www.openslr.org/resources/53/utt_spk_text.tsv -O $openslr_data_dir/SLR53/utt_spk_text.tsv\nwget https://www.openslr.org/resources/53/asr_bengali_0.zip -O $openslr_data_dir/SLR53/asr_bengali_0.zip\nwget https://www.openslr.org/resources/53/asr_bengali_1.zip -O $openslr_data_dir/SLR53/asr_bengali_1.zip\nwget https://www.openslr.org/resources/53/asr_bengali_2.zip -O $openslr_data_dir/SLR53/asr_bengali_2.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch51 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch51",
        bash_command="wget https://www.openslr.org/resources/53/asr_bengali_3.zip -O $openslr_data_dir/SLR53/asr_bengali_3.zip\nwget https://www.openslr.org/resources/53/asr_bengali_4.zip -O $openslr_data_dir/SLR53/asr_bengali_4.zip\nwget https://www.openslr.org/resources/53/asr_bengali_5.zip -O $openslr_data_dir/SLR53/asr_bengali_5.zip\nwget https://www.openslr.org/resources/53/asr_bengali_6.zip -O $openslr_data_dir/SLR53/asr_bengali_6.zip\nwget https://www.openslr.org/resources/53/asr_bengali_7.zip -O $openslr_data_dir/SLR53/asr_bengali_7.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch52 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch52",
        bash_command="wget https://www.openslr.org/resources/53/asr_bengali_8.zip -O $openslr_data_dir/SLR53/asr_bengali_8.zip\nwget https://www.openslr.org/resources/53/asr_bengali_9.zip -O $openslr_data_dir/SLR53/asr_bengali_9.zip\nwget https://www.openslr.org/resources/53/asr_bengali_a.zip -O $openslr_data_dir/SLR53/asr_bengali_a.zip\nwget https://www.openslr.org/resources/53/asr_bengali_b.zip -O $openslr_data_dir/SLR53/asr_bengali_b.zip\nwget https://www.openslr.org/resources/53/asr_bengali_c.zip -O $openslr_data_dir/SLR53/asr_bengali_c.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch53 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch53",
        bash_command="wget https://www.openslr.org/resources/53/asr_bengali_d.zip -O $openslr_data_dir/SLR53/asr_bengali_d.zip\nwget https://www.openslr.org/resources/53/asr_bengali_e.zip -O $openslr_data_dir/SLR53/asr_bengali_e.zip\nwget https://www.openslr.org/resources/53/asr_bengali_f.zip -O $openslr_data_dir/SLR53/asr_bengali_f.zip\nwget https://www.openslr.org/resources/54/about.html -O $openslr_data_dir/SLR54/about.html\nwget https://www.openslr.org/resources/54/LICENSE -O $openslr_data_dir/SLR54/LICENSE\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch54 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch54",
        bash_command="wget https://www.openslr.org/resources/54/utt_spk_text.tsv -O $openslr_data_dir/SLR54/utt_spk_text.tsv\nwget https://www.openslr.org/resources/54/asr_nepali_0.zip -O $openslr_data_dir/SLR54/asr_nepali_0.zip\nwget https://www.openslr.org/resources/54/asr_nepali_1.zip -O $openslr_data_dir/SLR54/asr_nepali_1.zip\nwget https://www.openslr.org/resources/54/asr_nepali_2.zip -O $openslr_data_dir/SLR54/asr_nepali_2.zip\nwget https://www.openslr.org/resources/54/asr_nepali_3.zip -O $openslr_data_dir/SLR54/asr_nepali_3.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch55 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch55",
        bash_command="wget https://www.openslr.org/resources/54/asr_nepali_4.zip -O $openslr_data_dir/SLR54/asr_nepali_4.zip\nwget https://www.openslr.org/resources/54/asr_nepali_5.zip -O $openslr_data_dir/SLR54/asr_nepali_5.zip\nwget https://www.openslr.org/resources/54/asr_nepali_6.zip -O $openslr_data_dir/SLR54/asr_nepali_6.zip\nwget https://www.openslr.org/resources/54/asr_nepali_7.zip -O $openslr_data_dir/SLR54/asr_nepali_7.zip\nwget https://www.openslr.org/resources/54/asr_nepali_8.zip -O $openslr_data_dir/SLR54/asr_nepali_8.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch56 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch56",
        bash_command="wget https://www.openslr.org/resources/54/asr_nepali_9.zip -O $openslr_data_dir/SLR54/asr_nepali_9.zip\nwget https://www.openslr.org/resources/54/asr_nepali_a.zip -O $openslr_data_dir/SLR54/asr_nepali_a.zip\nwget https://www.openslr.org/resources/54/asr_nepali_b.zip -O $openslr_data_dir/SLR54/asr_nepali_b.zip\nwget https://www.openslr.org/resources/54/asr_nepali_c.zip -O $openslr_data_dir/SLR54/asr_nepali_c.zip\nwget https://www.openslr.org/resources/54/asr_nepali_d.zip -O $openslr_data_dir/SLR54/asr_nepali_d.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch57 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch57",
        bash_command="wget https://www.openslr.org/resources/54/asr_nepali_e.zip -O $openslr_data_dir/SLR54/asr_nepali_e.zip\nwget https://www.openslr.org/resources/54/asr_nepali_f.zip -O $openslr_data_dir/SLR54/asr_nepali_f.zip\nwget https://www.openslr.org/resources/55/train.tgz -O $openslr_data_dir/SLR55/train.tgz\nwget https://www.openslr.org/resources/55/test.tgz -O $openslr_data_dir/SLR55/test.tgz\nwget https://www.openslr.org/resources/56/splits.zip -O $openslr_data_dir/SLR56/splits.zip\nwget https://www.openslr.org/resources/57/African_Accented_French.tar.gz -O $openslr_data_dir/SLR57/African_Accented_French.tar.gz\nwget https://www.openslr.org/resources/58/pansori-tedxkr-corpus-1.0.tar.gz -O $openslr_data_dir/SLR58/pansori-tedxkr-corpus-1.0.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch58 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch58",
        bash_command="wget https://www.openslr.org/resources/59/parlament_v1.0_clean.tar.gz -O $openslr_data_dir/SLR59/parlament_v1.0_clean.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch59 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch59",
        bash_command="wget https://www.openslr.org/resources/59/parlament_v1.0_other.tar.gz -O $openslr_data_dir/SLR59/parlament_v1.0_other.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch60 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch60",
        bash_command="wget https://www.openslr.org/resources/60/dev-clean.tar.gz -O $openslr_data_dir/SLR60/dev-clean.tar.gz\nwget https://www.openslr.org/resources/60/dev-other.tar.gz -O $openslr_data_dir/SLR60/dev-other.tar.gz\nwget https://www.openslr.org/resources/60/test-clean.tar.gz -O $openslr_data_dir/SLR60/test-clean.tar.gz\nwget https://www.openslr.org/resources/60/test-other.tar.gz -O $openslr_data_dir/SLR60/test-other.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch61 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch61",
        bash_command="wget https://www.openslr.org/resources/60/train-clean-100.tar.gz -O $openslr_data_dir/SLR60/train-clean-100.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch62 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch62",
        bash_command="wget https://www.openslr.org/resources/60/train-clean-360.tar.gz -O $openslr_data_dir/SLR60/train-clean-360.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch63 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch63",
        bash_command="wget https://www.openslr.org/resources/60/train-other-500.tar.gz -O $openslr_data_dir/SLR60/train-other-500.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch64 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch64",
        bash_command="wget https://www.openslr.org/resources/61/about.html -O $openslr_data_dir/SLR61/about.html\nwget https://www.openslr.org/resources/61/LICENSE -O $openslr_data_dir/SLR61/LICENSE\nwget https://www.openslr.org/resources/61/line_index_female.tsv -O $openslr_data_dir/SLR61/line_index_female.tsv\nwget https://www.openslr.org/resources/61/line_index_male.tsv -O $openslr_data_dir/SLR61/line_index_male.tsv\nwget https://www.openslr.org/resources/61/es_es_line_index_weather.tsv -O $openslr_data_dir/SLR61/es_es_line_index_weather.tsv\nwget https://www.openslr.org/resources/61/es_ar_line_index_weather.tsv -O $openslr_data_dir/SLR61/es_ar_line_index_weather.tsv\nwget https://www.openslr.org/resources/61/es_ar_female.zip -O $openslr_data_dir/SLR61/es_ar_female.zip\nwget https://www.openslr.org/resources/61/es_ar_male.zip -O $openslr_data_dir/SLR61/es_ar_male.zip\nwget https://www.openslr.org/resources/61/es_weather_messages.zip -O $openslr_data_dir/SLR61/es_weather_messages.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch65 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch65",
        bash_command="wget https://www.openslr.org/resources/62/aidatatang_200zh.tgz -O $openslr_data_dir/SLR62/aidatatang_200zh.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch66 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch66",
        bash_command="wget https://www.openslr.org/resources/63/about.html -O $openslr_data_dir/SLR63/about.html\nwget https://www.openslr.org/resources/63/LICENSE -O $openslr_data_dir/SLR63/LICENSE\nwget https://www.openslr.org/resources/63/line_index_female.tsv -O $openslr_data_dir/SLR63/line_index_female.tsv\nwget https://www.openslr.org/resources/63/line_index_male.tsv -O $openslr_data_dir/SLR63/line_index_male.tsv\nwget https://www.openslr.org/resources/63/ml_in_female.zip -O $openslr_data_dir/SLR63/ml_in_female.zip\nwget https://www.openslr.org/resources/63/ml_in_male.zip -O $openslr_data_dir/SLR63/ml_in_male.zip\nwget https://www.openslr.org/resources/64/about.html -O $openslr_data_dir/SLR64/about.html\nwget https://www.openslr.org/resources/64/LICENSE -O $openslr_data_dir/SLR64/LICENSE\nwget https://www.openslr.org/resources/64/line_index.tsv -O $openslr_data_dir/SLR64/line_index.tsv\nwget https://www.openslr.org/resources/64/mr_in_female.zip -O $openslr_data_dir/SLR64/mr_in_female.zip\nwget https://www.openslr.org/resources/65/about.html -O $openslr_data_dir/SLR65/about.html\nwget https://www.openslr.org/resources/65/LICENSE -O $openslr_data_dir/SLR65/LICENSE\nwget https://www.openslr.org/resources/65/line_index_female.tsv -O $openslr_data_dir/SLR65/line_index_female.tsv\nwget https://www.openslr.org/resources/65/line_index_male.tsv -O $openslr_data_dir/SLR65/line_index_male.tsv\nwget https://www.openslr.org/resources/65/ta_in_female.zip -O $openslr_data_dir/SLR65/ta_in_female.zip\nwget https://www.openslr.org/resources/65/ta_in_male.zip -O $openslr_data_dir/SLR65/ta_in_male.zip\nwget https://www.openslr.org/resources/66/about.html -O $openslr_data_dir/SLR66/about.html\nwget https://www.openslr.org/resources/66/LICENSE -O $openslr_data_dir/SLR66/LICENSE\nwget https://www.openslr.org/resources/66/line_index_female.tsv -O $openslr_data_dir/SLR66/line_index_female.tsv\nwget https://www.openslr.org/resources/66/line_index_male.tsv -O $openslr_data_dir/SLR66/line_index_male.tsv\nwget https://www.openslr.org/resources/66/te_in_female.zip -O $openslr_data_dir/SLR66/te_in_female.zip\nwget https://www.openslr.org/resources/66/te_in_male.zip -O $openslr_data_dir/SLR66/te_in_male.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch67 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch67",
        bash_command="wget https://www.openslr.org/resources/67/tedx_spanish_corpus.tgz -O $openslr_data_dir/SLR67/tedx_spanish_corpus.tgz\nwget https://www.openslr.org/resources/68/dev_set.tar.gz -O $openslr_data_dir/SLR68/dev_set.tar.gz\nwget https://www.openslr.org/resources/68/test_set.tar.gz -O $openslr_data_dir/SLR68/test_set.tar.gz\nwget https://www.openslr.org/resources/68/metadata.tar.gz -O $openslr_data_dir/SLR68/metadata.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch68 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch68",
        bash_command="wget https://www.openslr.org/resources/69/about.html -O $openslr_data_dir/SLR69/about.html\nwget https://www.openslr.org/resources/69/LICENSE -O $openslr_data_dir/SLR69/LICENSE\nwget https://www.openslr.org/resources/69/line_index_female.tsv -O $openslr_data_dir/SLR69/line_index_female.tsv\nwget https://www.openslr.org/resources/69/line_index_male.tsv -O $openslr_data_dir/SLR69/line_index_male.tsv\nwget https://www.openslr.org/resources/69/ca_es_female.zip -O $openslr_data_dir/SLR69/ca_es_female.zip\nwget https://www.openslr.org/resources/69/ca_es_male.zip -O $openslr_data_dir/SLR69/ca_es_male.zip\nwget https://www.openslr.org/resources/70/about.html -O $openslr_data_dir/SLR70/about.html\nwget https://www.openslr.org/resources/70/LICENSE -O $openslr_data_dir/SLR70/LICENSE\nwget https://www.openslr.org/resources/70/line_index_female.tsv -O $openslr_data_dir/SLR70/line_index_female.tsv\nwget https://www.openslr.org/resources/70/line_index_male.tsv -O $openslr_data_dir/SLR70/line_index_male.tsv\nwget https://www.openslr.org/resources/70/en_ng_female.zip -O $openslr_data_dir/SLR70/en_ng_female.zip\nwget https://www.openslr.org/resources/70/en_ng_male.zip -O $openslr_data_dir/SLR70/en_ng_male.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch69 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch69",
        bash_command="wget https://www.openslr.org/resources/71/about.html -O $openslr_data_dir/SLR71/about.html\nwget https://www.openslr.org/resources/71/LICENSE -O $openslr_data_dir/SLR71/LICENSE\nwget https://www.openslr.org/resources/71/line_index_female.tsv -O $openslr_data_dir/SLR71/line_index_female.tsv\nwget https://www.openslr.org/resources/71/line_index_male.tsv -O $openslr_data_dir/SLR71/line_index_male.tsv\nwget https://www.openslr.org/resources/71/es_cl_female.zip -O $openslr_data_dir/SLR71/es_cl_female.zip\nwget https://www.openslr.org/resources/71/es_cl_male.zip -O $openslr_data_dir/SLR71/es_cl_male.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch70 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch70",
        bash_command="wget https://www.openslr.org/resources/72/about.html -O $openslr_data_dir/SLR72/about.html\nwget https://www.openslr.org/resources/72/LICENSE -O $openslr_data_dir/SLR72/LICENSE\nwget https://www.openslr.org/resources/72/line_index_female.tsv -O $openslr_data_dir/SLR72/line_index_female.tsv\nwget https://www.openslr.org/resources/72/line_index_male.tsv -O $openslr_data_dir/SLR72/line_index_male.tsv\nwget https://www.openslr.org/resources/72/es_co_female.zip -O $openslr_data_dir/SLR72/es_co_female.zip\nwget https://www.openslr.org/resources/72/es_co_male.zip -O $openslr_data_dir/SLR72/es_co_male.zip\nwget https://www.openslr.org/resources/73/about.html -O $openslr_data_dir/SLR73/about.html\nwget https://www.openslr.org/resources/73/LICENSE -O $openslr_data_dir/SLR73/LICENSE\nwget https://www.openslr.org/resources/73/line_index_female.tsv -O $openslr_data_dir/SLR73/line_index_female.tsv\nwget https://www.openslr.org/resources/73/line_index_male.tsv -O $openslr_data_dir/SLR73/line_index_male.tsv\nwget https://www.openslr.org/resources/73/es_pe_female.zip -O $openslr_data_dir/SLR73/es_pe_female.zip\nwget https://www.openslr.org/resources/73/es_pe_male.zip -O $openslr_data_dir/SLR73/es_pe_male.zip\nwget https://www.openslr.org/resources/74/about.html -O $openslr_data_dir/SLR74/about.html\nwget https://www.openslr.org/resources/74/LICENSE -O $openslr_data_dir/SLR74/LICENSE\nwget https://www.openslr.org/resources/74/line_index_female.tsv -O $openslr_data_dir/SLR74/line_index_female.tsv\nwget https://www.openslr.org/resources/74/es_pr_female.zip -O $openslr_data_dir/SLR74/es_pr_female.zip\nwget https://www.openslr.org/resources/75/about.html -O $openslr_data_dir/SLR75/about.html\nwget https://www.openslr.org/resources/75/LICENSE -O $openslr_data_dir/SLR75/LICENSE\nwget https://www.openslr.org/resources/75/line_index_female.tsv -O $openslr_data_dir/SLR75/line_index_female.tsv\nwget https://www.openslr.org/resources/75/line_index_male.tsv -O $openslr_data_dir/SLR75/line_index_male.tsv\nwget https://www.openslr.org/resources/75/es_ve_female.zip -O $openslr_data_dir/SLR75/es_ve_female.zip\nwget https://www.openslr.org/resources/75/es_ve_male.zip -O $openslr_data_dir/SLR75/es_ve_male.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch71 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch71",
        bash_command="wget https://www.openslr.org/resources/76/about.html -O $openslr_data_dir/SLR76/about.html\nwget https://www.openslr.org/resources/76/LICENSE -O $openslr_data_dir/SLR76/LICENSE\nwget https://www.openslr.org/resources/76/line_index_female.tsv -O $openslr_data_dir/SLR76/line_index_female.tsv\nwget https://www.openslr.org/resources/76/line_index_male.tsv -O $openslr_data_dir/SLR76/line_index_male.tsv\nwget https://www.openslr.org/resources/76/eu_es_female.zip -O $openslr_data_dir/SLR76/eu_es_female.zip\nwget https://www.openslr.org/resources/76/eu_es_male.zip -O $openslr_data_dir/SLR76/eu_es_male.zip\nwget https://www.openslr.org/resources/77/about.html -O $openslr_data_dir/SLR77/about.html\nwget https://www.openslr.org/resources/77/LICENSE -O $openslr_data_dir/SLR77/LICENSE\nwget https://www.openslr.org/resources/77/line_index_female.tsv -O $openslr_data_dir/SLR77/line_index_female.tsv\nwget https://www.openslr.org/resources/77/line_index_male.tsv -O $openslr_data_dir/SLR77/line_index_male.tsv\nwget https://www.openslr.org/resources/77/gl_es_female.zip -O $openslr_data_dir/SLR77/gl_es_female.zip\nwget https://www.openslr.org/resources/77/gl_es_male.zip -O $openslr_data_dir/SLR77/gl_es_male.zip\nwget https://www.openslr.org/resources/78/about.html -O $openslr_data_dir/SLR78/about.html\nwget https://www.openslr.org/resources/78/LICENSE -O $openslr_data_dir/SLR78/LICENSE\nwget https://www.openslr.org/resources/78/line_index_female.tsv -O $openslr_data_dir/SLR78/line_index_female.tsv\nwget https://www.openslr.org/resources/78/line_index_male.tsv -O $openslr_data_dir/SLR78/line_index_male.tsv\nwget https://www.openslr.org/resources/78/gu_in_female.zip -O $openslr_data_dir/SLR78/gu_in_female.zip\nwget https://www.openslr.org/resources/78/gu_in_male.zip -O $openslr_data_dir/SLR78/gu_in_male.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch72 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch72",
        bash_command="wget https://www.openslr.org/resources/79/about.html -O $openslr_data_dir/SLR79/about.html\nwget https://www.openslr.org/resources/79/LICENSE -O $openslr_data_dir/SLR79/LICENSE\nwget https://www.openslr.org/resources/79/line_index_female.tsv -O $openslr_data_dir/SLR79/line_index_female.tsv\nwget https://www.openslr.org/resources/79/line_index_male.tsv -O $openslr_data_dir/SLR79/line_index_male.tsv\nwget https://www.openslr.org/resources/79/kn_in_female.zip -O $openslr_data_dir/SLR79/kn_in_female.zip\nwget https://www.openslr.org/resources/79/kn_in_male.zip -O $openslr_data_dir/SLR79/kn_in_male.zip\nwget https://www.openslr.org/resources/80/about.html -O $openslr_data_dir/SLR80/about.html\nwget https://www.openslr.org/resources/80/LICENSE -O $openslr_data_dir/SLR80/LICENSE\nwget https://www.openslr.org/resources/80/line_index_female.tsv -O $openslr_data_dir/SLR80/line_index_female.tsv\nwget https://www.openslr.org/resources/80/my_mm_female.zip -O $openslr_data_dir/SLR80/my_mm_female.zip\nwget https://www.openslr.org/resources/81/samples.tar.gz -O $openslr_data_dir/SLR81/samples.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch73 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch73",
        bash_command="wget https://www.openslr.org/resources/82/cn-celeb_v2.tar.gz -O $openslr_data_dir/SLR82/cn-celeb_v2.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch74 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch74",
        bash_command="wget https://www.openslr.org/resources/82/cn-celeb2_v2.tar.gzaa -O $openslr_data_dir/SLR82/cn-celeb2_v2.tar.gzaa\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch75 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch75",
        bash_command="wget https://www.openslr.org/resources/82/cn-celeb2_v2.tar.gzab -O $openslr_data_dir/SLR82/cn-celeb2_v2.tar.gzab\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch76 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch76",
        bash_command="wget https://www.openslr.org/resources/82/cn-celeb2_v2.tar.gzac -O $openslr_data_dir/SLR82/cn-celeb2_v2.tar.gzac\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch77 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch77",
        bash_command="wget https://www.openslr.org/resources/83/about.html -O $openslr_data_dir/SLR83/about.html\nwget https://www.openslr.org/resources/83/LICENSE -O $openslr_data_dir/SLR83/LICENSE\nwget https://www.openslr.org/resources/83/line_index_all.csv -O $openslr_data_dir/SLR83/line_index_all.csv\nwget https://www.openslr.org/resources/83/dialect_info.txt -O $openslr_data_dir/SLR83/dialect_info.txt\nwget https://www.openslr.org/resources/83/irish_english_male.zip -O $openslr_data_dir/SLR83/irish_english_male.zip\nwget https://www.openslr.org/resources/83/midlands_english_female.zip -O $openslr_data_dir/SLR83/midlands_english_female.zip\nwget https://www.openslr.org/resources/83/midlands_english_male.zip -O $openslr_data_dir/SLR83/midlands_english_male.zip\nwget https://www.openslr.org/resources/83/northern_english_female.zip -O $openslr_data_dir/SLR83/northern_english_female.zip\nwget https://www.openslr.org/resources/83/northern_english_male.zip -O $openslr_data_dir/SLR83/northern_english_male.zip\nwget https://www.openslr.org/resources/83/scottish_english_female.zip -O $openslr_data_dir/SLR83/scottish_english_female.zip\nwget https://www.openslr.org/resources/83/scottish_english_male.zip -O $openslr_data_dir/SLR83/scottish_english_male.zip\nwget https://www.openslr.org/resources/83/southern_english_female.zip -O $openslr_data_dir/SLR83/southern_english_female.zip\nwget https://www.openslr.org/resources/83/southern_english_male.zip -O $openslr_data_dir/SLR83/southern_english_male.zip\nwget https://www.openslr.org/resources/83/welsh_english_female.zip -O $openslr_data_dir/SLR83/welsh_english_female.zip\nwget https://www.openslr.org/resources/83/welsh_english_male.zip -O $openslr_data_dir/SLR83/welsh_english_male.zip\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch78 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch78",
        bash_command="wget https://www.openslr.org/resources/84/scribblelens.corpus.v1.2.zip -O $openslr_data_dir/SLR84/scribblelens.corpus.v1.2.zip\nwget https://www.openslr.org/resources/84/scribblelens.supplement.original.pages.tgz -O $openslr_data_dir/SLR84/scribblelens.supplement.original.pages.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch79 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch79",
        bash_command="wget https://www.openslr.org/resources/85/train.tar.gz -O $openslr_data_dir/SLR85/train.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch80 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch80",
        bash_command="wget https://www.openslr.org/resources/85/dev.tar.gz -O $openslr_data_dir/SLR85/dev.tar.gz\nwget https://www.openslr.org/resources/85/test.tar.gz -O $openslr_data_dir/SLR85/test.tar.gz\nwget https://www.openslr.org/resources/85/test_v2.tar.gz -O $openslr_data_dir/SLR85/test_v2.tar.gz\nwget https://www.openslr.org/resources/85/filename_mapping.tar.gz -O $openslr_data_dir/SLR85/filename_mapping.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch81 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch81",
        bash_command="wget https://www.openslr.org/resources/86/about.html -O $openslr_data_dir/SLR86/about.html\nwget https://www.openslr.org/resources/86/LICENSE -O $openslr_data_dir/SLR86/LICENSE\nwget https://www.openslr.org/resources/86/line_index_female.tsv -O $openslr_data_dir/SLR86/line_index_female.tsv\nwget https://www.openslr.org/resources/86/line_index_male.tsv -O $openslr_data_dir/SLR86/line_index_male.tsv\nwget https://www.openslr.org/resources/86/yo_ng_female.zip -O $openslr_data_dir/SLR86/yo_ng_female.zip\nwget https://www.openslr.org/resources/86/yo_ng_male.zip -O $openslr_data_dir/SLR86/yo_ng_male.zip\nwget https://www.openslr.org/resources/86/annotation_info.txt -O $openslr_data_dir/SLR86/annotation_info.txt\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch82 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch82",
        bash_command="wget https://www.openslr.org/resources/87/mobvoi_hotword_dataset.tgz -O $openslr_data_dir/SLR87/mobvoi_hotword_dataset.tgz\nwget https://www.openslr.org/resources/87/mobvoi_hotword_dataset_resources.tgz -O $openslr_data_dir/SLR87/mobvoi_hotword_dataset_resources.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch83 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch83",
        bash_command="wget https://www.openslr.org/resources/88/wav.tgz -O $openslr_data_dir/SLR88/wav.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch84 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch84",
        bash_command="wget https://www.openslr.org/resources/88/txt.tgz -O $openslr_data_dir/SLR88/txt.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch85 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch85",
        bash_command="wget https://www.openslr.org/resources/89/Yoloxochitl-Mixtec-Manifest.tgz -O $openslr_data_dir/SLR89/Yoloxochitl-Mixtec-Manifest.tgz\nwget https://www.openslr.org/resources/89/Novice-Transcription-Correction.zip -O $openslr_data_dir/SLR89/Novice-Transcription-Correction.zip\nwget https://www.openslr.org/resources/92/Puebla-Nahuatl-Manifest.tgz -O $openslr_data_dir/SLR92/Puebla-Nahuatl-Manifest.tgz\nwget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part00 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part00\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch86 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch86",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part01 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part01\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch87 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch87",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part02 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part02\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch88 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch88",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part03 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part03\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch89 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch89",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part04 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part04\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch90 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch90",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part05 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part05\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch91 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch91",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part06 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part06\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch92 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch92",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part07 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part07\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch93 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch93",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part08 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part08\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch94 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch94",
        bash_command="wget https://www.openslr.org/resources/92/Sound-Files-Puebla-Nahuatl.tgz.part09 -O $openslr_data_dir/SLR92/Sound-Files-Puebla-Nahuatl.tgz.part09\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch95 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch95",
        bash_command="wget https://www.openslr.org/resources/92/SpeechTranslation_Nahuatl_Manifest.tgz -O $openslr_data_dir/SLR92/SpeechTranslation_Nahuatl_Manifest.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch96 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch96",
        bash_command="wget https://www.openslr.org/resources/93/data_aishell3.tgz -O $openslr_data_dir/SLR93/data_aishell3.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch97 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch97",
        bash_command="wget https://www.openslr.org/resources/95/thorsten-de_v02.tgz -O $openslr_data_dir/SLR95/thorsten-de_v02.tgz\nwget https://www.openslr.org/resources/96/ruls_data.tar.gz -O $openslr_data_dir/SLR96/ruls_data.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch98 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch98",
        bash_command="wget https://www.openslr.org/resources/97/KoreanReadSpeechCorpus.tar.gz -O $openslr_data_dir/SLR97/KoreanReadSpeechCorpus.tar.gz\nwget https://www.openslr.org/resources/98/Parent-ChildVocalInteraction.tar.gz -O $openslr_data_dir/SLR98/Parent-ChildVocalInteraction.tar.gz\nwget https://www.openslr.org/resources/99/NonverbalVocalization.tgz -O $openslr_data_dir/SLR99/NonverbalVocalization.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch99 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch99",
        bash_command="wget https://www.openslr.org/resources/101/speechocean762.tar.gz -O $openslr_data_dir/SLR101/speechocean762.tar.gz\nwget https://www.openslr.org/resources/102/ISSAI_KSC_335RS_v1.1_flac.tar.gz -O $openslr_data_dir/SLR102/ISSAI_KSC_335RS_v1.1_flac.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch100 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch100",
        bash_command="wget https://www.openslr.org/resources/103/Hindi_train.tar.gz -O $openslr_data_dir/SLR103/Hindi_train.tar.gz\nwget https://www.openslr.org/resources/103/Hindi_test.tar.gz -O $openslr_data_dir/SLR103/Hindi_test.tar.gz\nwget https://www.openslr.org/resources/103/Marathi_train.tar.gz -O $openslr_data_dir/SLR103/Marathi_train.tar.gz\nwget https://www.openslr.org/resources/103/Marathi_test.tar.gz -O $openslr_data_dir/SLR103/Marathi_test.tar.gz\nwget https://www.openslr.org/resources/103/Odia_train.tar.gz -O $openslr_data_dir/SLR103/Odia_train.tar.gz\nwget https://www.openslr.org/resources/103/Odia_test.tar.gz -O $openslr_data_dir/SLR103/Odia_test.tar.gz\nwget https://www.openslr.org/resources/103/subtask1_blindtest_wReadme.tar.gz -O $openslr_data_dir/SLR103/subtask1_blindtest_wReadme.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch101 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch101",
        bash_command="wget https://www.openslr.org/resources/104/Hindi-English_train.tar.gz -O $openslr_data_dir/SLR104/Hindi-English_train.tar.gz\nwget https://www.openslr.org/resources/104/Hindi-English_test.tar.gz -O $openslr_data_dir/SLR104/Hindi-English_test.tar.gz\nwget https://www.openslr.org/resources/104/Bengali-English_train.tar.gz -O $openslr_data_dir/SLR104/Bengali-English_train.tar.gz\nwget https://www.openslr.org/resources/104/Bengali-English_test.tar.gz -O $openslr_data_dir/SLR104/Bengali-English_test.tar.gz\nwget https://www.openslr.org/resources/104/subtask2_blindtest_wReadme.tar.gz -O $openslr_data_dir/SLR104/subtask2_blindtest_wReadme.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch102 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch102",
        bash_command="wget https://www.openslr.org/resources/105/nicolingua-0003-west-african-radio-corpus.tgz -O $openslr_data_dir/SLR105/nicolingua-0003-west-african-radio-corpus.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch103 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch103",
        bash_command="wget https://www.openslr.org/resources/106/nicolingua-0004-west-african-va-asr-corpus.tgz -O $openslr_data_dir/SLR106/nicolingua-0004-west-african-va-asr-corpus.tgz\nwget https://www.openslr.org/resources/107/Deposit-Totonaco-for-ASR-Community.pdf -O $openslr_data_dir/SLR107/Deposit-Totonaco-for-ASR-Community.pdf\nwget https://www.openslr.org/resources/107/Amith-Lopez_Totonac-recordings-northern-Puebla-and-adjacent-Veracruz_Metadata.xml -O $openslr_data_dir/SLR107/Amith-Lopez_Totonac-recordings-northern-Puebla-and-adjacent-Veracruz_Metadata.xml\nwget https://www.openslr.org/resources/107/Totonac_Corpus.tgz -O $openslr_data_dir/SLR107/Totonac_Corpus.tgz\nwget https://www.openslr.org/resources/108/AR.tgz -O $openslr_data_dir/SLR108/AR.tgz\nwget https://www.openslr.org/resources/108/ES.tgz -O $openslr_data_dir/SLR108/ES.tgz\nwget https://www.openslr.org/resources/108/FR.tgz -O $openslr_data_dir/SLR108/FR.tgz\nwget https://www.openslr.org/resources/108/TR.tgz -O $openslr_data_dir/SLR108/TR.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch104 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch104",
        bash_command="wget https://www.openslr.org/resources/100/mtedx_es.tgz -O $openslr_data_dir/SLR100/mtedx_es.tgz\nwget https://www.openslr.org/resources/100/mtedx_fr.tgz -O $openslr_data_dir/SLR100/mtedx_fr.tgz\nwget https://www.openslr.org/resources/100/mtedx_pt.tgz -O $openslr_data_dir/SLR100/mtedx_pt.tgz\nwget https://www.openslr.org/resources/100/mtedx_it.tgz -O $openslr_data_dir/SLR100/mtedx_it.tgz\nwget https://www.openslr.org/resources/100/mtedx_ru.tgz -O $openslr_data_dir/SLR100/mtedx_ru.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch105 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch105",
        bash_command="wget https://www.openslr.org/resources/100/mtedx_el.tgz -O $openslr_data_dir/SLR100/mtedx_el.tgz\nwget https://www.openslr.org/resources/100/mtedx_ar.tgz -O $openslr_data_dir/SLR100/mtedx_ar.tgz\nwget https://www.openslr.org/resources/100/mtedx_de.tgz -O $openslr_data_dir/SLR100/mtedx_de.tgz\nwget https://www.openslr.org/resources/100/mtedx_es-en.tgz -O $openslr_data_dir/SLR100/mtedx_es-en.tgz\nwget https://www.openslr.org/resources/100/mtedx_es-fr.tgz -O $openslr_data_dir/SLR100/mtedx_es-fr.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch106 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch106",
        bash_command="wget https://www.openslr.org/resources/100/mtedx_es-it.tgz -O $openslr_data_dir/SLR100/mtedx_es-it.tgz\nwget https://www.openslr.org/resources/100/mtedx_es-pt.tgz -O $openslr_data_dir/SLR100/mtedx_es-pt.tgz\nwget https://www.openslr.org/resources/100/mtedx_fr-en.tgz -O $openslr_data_dir/SLR100/mtedx_fr-en.tgz\nwget https://www.openslr.org/resources/100/mtedx_fr-es.tgz -O $openslr_data_dir/SLR100/mtedx_fr-es.tgz\nwget https://www.openslr.org/resources/100/mtedx_fr-pt.tgz -O $openslr_data_dir/SLR100/mtedx_fr-pt.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch107 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch107",
        bash_command="wget https://www.openslr.org/resources/100/mtedx_pt-en.tgz -O $openslr_data_dir/SLR100/mtedx_pt-en.tgz\nwget https://www.openslr.org/resources/100/mtedx_pt-es.tgz -O $openslr_data_dir/SLR100/mtedx_pt-es.tgz\nwget https://www.openslr.org/resources/100/mtedx_it-en.tgz -O $openslr_data_dir/SLR100/mtedx_it-en.tgz\nwget https://www.openslr.org/resources/100/mtedx_it-es.tgz -O $openslr_data_dir/SLR100/mtedx_it-es.tgz\nwget https://www.openslr.org/resources/100/mtedx_ru-en.tgz -O $openslr_data_dir/SLR100/mtedx_ru-en.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch108 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch108",
        bash_command="wget https://www.openslr.org/resources/100/mtedx_el-en.tgz -O $openslr_data_dir/SLR100/mtedx_el-en.tgz\nwget https://www.openslr.org/resources/100/mtedx_iwslt2021.tgz -O $openslr_data_dir/SLR100/mtedx_iwslt2021.tgz\nwget https://www.openslr.org/resources/100/MTEDx-french-talks-gender-annotation.csv -O $openslr_data_dir/SLR100/MTEDx-french-talks-gender-annotation.csv\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch109 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch109",
        bash_command="wget https://www.openslr.org/resources/109/hi_fi_tts_v0.tar.gz -O $openslr_data_dir/SLR109/hi_fi_tts_v0.tar.gz\nwget https://www.openslr.org/resources/110/thorsten-emotional_v02.tgz -O $openslr_data_dir/SLR110/thorsten-emotional_v02.tgz\nwget https://www.openslr.org/resources/111/train_L.tar.gz -O $openslr_data_dir/SLR111/train_L.tar.gz\nwget https://www.openslr.org/resources/111/train_M.tar.gz -O $openslr_data_dir/SLR111/train_M.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch110 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch110",
        bash_command="wget https://www.openslr.org/resources/111/train_S.tar.gz -O $openslr_data_dir/SLR111/train_S.tar.gz\nwget https://www.openslr.org/resources/111/test.tar.gz -O $openslr_data_dir/SLR111/test.tar.gz\nwget https://www.openslr.org/resources/112/samromur_21.05.tgz -O $openslr_data_dir/SLR112/samromur_21.05.tgz\nwget https://www.openslr.org/resources/113/readme.tgz -O $openslr_data_dir/SLR113/readme.tgz\nwget https://www.openslr.org/resources/113/label.tgz -O $openslr_data_dir/SLR113/label.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch111 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch111",
        bash_command="wget https://www.openslr.org/resources/113/sound.tgz -O $openslr_data_dir/SLR113/sound.tgz\nwget https://www.openslr.org/resources/114/golos_opus.tar.gz -O $openslr_data_dir/SLR114/golos_opus.tar.gz\nwget https://www.openslr.org/resources/114/QuartzNet15x5_golos.nemo.gz -O $openslr_data_dir/SLR114/QuartzNet15x5_golos.nemo.gz\nwget https://www.openslr.org/resources/114/kenlms.tar.gz -O $openslr_data_dir/SLR114/kenlms.tar.gz\nwget https://www.openslr.org/resources/115/bea_Amused.tar.gz -O $openslr_data_dir/SLR115/bea_Amused.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch112 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch112",
        bash_command="wget https://www.openslr.org/resources/115/bea_Angry.tar.gz -O $openslr_data_dir/SLR115/bea_Angry.tar.gz\nwget https://www.openslr.org/resources/115/bea_Disgusted.tar.gz -O $openslr_data_dir/SLR115/bea_Disgusted.tar.gz\nwget https://www.openslr.org/resources/115/bea_Neutral.tar.gz -O $openslr_data_dir/SLR115/bea_Neutral.tar.gz\nwget https://www.openslr.org/resources/115/bea_Sleepy.tar.gz -O $openslr_data_dir/SLR115/bea_Sleepy.tar.gz\nwget https://www.openslr.org/resources/115/jenie_Amused.tar.gz -O $openslr_data_dir/SLR115/jenie_Amused.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch113 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch113",
        bash_command="wget https://www.openslr.org/resources/115/jenie_Angry.tar.gz -O $openslr_data_dir/SLR115/jenie_Angry.tar.gz\nwget https://www.openslr.org/resources/115/jenie_Disgusted.tar.gz -O $openslr_data_dir/SLR115/jenie_Disgusted.tar.gz\nwget https://www.openslr.org/resources/115/jenie_Neutral.tar.gz -O $openslr_data_dir/SLR115/jenie_Neutral.tar.gz\nwget https://www.openslr.org/resources/115/jenie_Sleepy.tar.gz -O $openslr_data_dir/SLR115/jenie_Sleepy.tar.gz\nwget https://www.openslr.org/resources/115/josh_Amused.tar.gz -O $openslr_data_dir/SLR115/josh_Amused.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch114 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch114",
        bash_command="wget https://www.openslr.org/resources/115/josh_Neutral.tar.gz -O $openslr_data_dir/SLR115/josh_Neutral.tar.gz\nwget https://www.openslr.org/resources/115/josh_Sleepy.tar.gz -O $openslr_data_dir/SLR115/josh_Sleepy.tar.gz\nwget https://www.openslr.org/resources/115/sam_Amused.tar.gz -O $openslr_data_dir/SLR115/sam_Amused.tar.gz\nwget https://www.openslr.org/resources/115/sam_Angry.tar.gz -O $openslr_data_dir/SLR115/sam_Angry.tar.gz\nwget https://www.openslr.org/resources/115/sam_Disgusted.tar.gz -O $openslr_data_dir/SLR115/sam_Disgusted.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch115 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch115",
        bash_command="wget https://www.openslr.org/resources/115/sam_Neutral.tar.gz -O $openslr_data_dir/SLR115/sam_Neutral.tar.gz\nwget https://www.openslr.org/resources/115/sam_Sleepy.tar.gz -O $openslr_data_dir/SLR115/sam_Sleepy.tar.gz\nwget https://www.openslr.org/resources/116/samromur_queries_21.12.zip -O $openslr_data_dir/SLR116/samromur_queries_21.12.zip\nwget https://www.openslr.org/resources/117/samromur_children_21.09.zip -O $openslr_data_dir/SLR117/samromur_children_21.09.zip\nwget https://www.openslr.org/resources/118/GV_Train_100h.tar.gz -O $openslr_data_dir/SLR118/GV_Train_100h.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch116 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch116",
        bash_command="wget https://www.openslr.org/resources/118/GV_Dev_5h.tar.gz -O $openslr_data_dir/SLR118/GV_Dev_5h.tar.gz\nwget https://www.openslr.org/resources/118/GV_Eval_3h.tar.gz -O $openslr_data_dir/SLR118/GV_Eval_3h.tar.gz\nwget https://www.openslr.org/resources/118/Gramvaani_1000hrData_Part1.tar.gz -O $openslr_data_dir/SLR118/Gramvaani_1000hrData_Part1.tar.gz\nwget https://www.openslr.org/resources/118/Gramvaani_1000hrData_Part2.tar.gz -O $openslr_data_dir/SLR118/Gramvaani_1000hrData_Part2.tar.gz\nwget https://www.openslr.org/resources/118/Gramvaani_1000hrData_Part3.tar.gz -O $openslr_data_dir/SLR118/Gramvaani_1000hrData_Part3.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch117 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch117",
        bash_command="wget https://www.openslr.org/resources/118/Gramvaani_1000hrData_Part4.tar.gz -O $openslr_data_dir/SLR118/Gramvaani_1000hrData_Part4.tar.gz\nwget https://www.openslr.org/resources/118/Gramvaani_1000hrData_Part5.tar.gz -O $openslr_data_dir/SLR118/Gramvaani_1000hrData_Part5.tar.gz\nwget https://www.openslr.org/resources/118/Metadata.tar.gz -O $openslr_data_dir/SLR118/Metadata.tar.gz\nwget https://speech-lab-share-data.oss-cn-shanghai.aliyuncs.com/AliMeeting/openlr/Train_Ali_near.tar.gz -O $openslr_data_dir/SLR119/Train_Ali_near.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch118 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch118",
        bash_command="wget https://speech-lab-share-data.oss-cn-shanghai.aliyuncs.com/AliMeeting/openlr/Eval_Ali.tar.gz -O $openslr_data_dir/SLR119/Eval_Ali.tar.gz\nwget https://speech-lab-share-data.oss-cn-shanghai.aliyuncs.com/AliMeeting/openlr/Test_Ali.tar.gz -O $openslr_data_dir/SLR119/Test_Ali.tar.gz\nwget https://www.openslr.org/resources/120/data.tgz -O $openslr_data_dir/SLR120/data.tgz\nwget https://www.openslr.org/resources/120/resource.tgz -O $openslr_data_dir/SLR120/resource.tgz\nwget https://www.openslr.org/resources/122/kashmiri.tar.gz -O $openslr_data_dir/SLR122/kashmiri.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch119 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch119",
        bash_command="wget https://www.openslr.org/resources/123/MagicData-RAMC.tar.gz -O $openslr_data_dir/SLR123/MagicData-RAMC.tar.gz\nwget https://www.openslr.org/resources/124/Tibetan_speech_data.tgz -O $openslr_data_dir/SLR124/Tibetan_speech_data.tgz\nwget https://www.openslr.org/resources/125/BLARK_1.0_update.tar.gz -O $openslr_data_dir/SLR125/BLARK_1.0_update.tar.gz\nwget https://www.openslr.org/resources/126/mile_kannada_train.tar.gz -O $openslr_data_dir/SLR126/mile_kannada_train.tar.gz\nwget https://www.openslr.org/resources/126/mile_kannada_test.tar.gz -O $openslr_data_dir/SLR126/mile_kannada_test.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch120 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch120",
        bash_command="wget https://www.openslr.org/resources/127/mile_tamil_asr_corpus.tar.gz -O $openslr_data_dir/SLR127/mile_tamil_asr_corpus.tar.gz\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.zip -O $openslr_data_dir/SLR128/samromur_unverified_22.07.zip\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.z01 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z01\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.z02 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z02\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.z03 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z03\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch121 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch121",
        bash_command="wget https://www.openslr.org/resources/128/samromur_unverified_22.07.z04 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z04\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.z05 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z05\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.z06 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z06\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.z07 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z07\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.z08 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z08\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch122 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch122",
        bash_command="wget https://www.openslr.org/resources/128/samromur_unverified_22.07.z09 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z09\nwget https://www.openslr.org/resources/128/samromur_unverified_22.07.z10 -O $openslr_data_dir/SLR128/samromur_unverified_22.07.z10\nwget https://www.openslr.org/resources/128/samromur_unverified_md5sums.txt -O $openslr_data_dir/SLR128/samromur_unverified_md5sums.txt\nwget https://www.openslr.org/resources/129/akuapem-twi.tgz -O $openslr_data_dir/SLR129/akuapem-twi.tgz\nwget https://www.openslr.org/resources/129/asante-twi.tgz -O $openslr_data_dir/SLR129/asante-twi.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch123 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch123",
        bash_command="wget https://www.openslr.org/resources/129/ewe.tgz -O $openslr_data_dir/SLR129/ewe.tgz\nwget https://www.openslr.org/resources/129/hausa.tgz -O $openslr_data_dir/SLR129/hausa.tgz\nwget https://www.openslr.org/resources/129/lingala.tgz -O $openslr_data_dir/SLR129/lingala.tgz\nwget https://www.openslr.org/resources/129/yoruba.tgz -O $openslr_data_dir/SLR129/yoruba.tgz\n",
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch124 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch124",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_german_opus.tar.gz -O $openslr_data_dir/SLR94/mls_german_opus.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch125 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch125",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_dutch_opus.tar.gz -O $openslr_data_dir/SLR94/mls_dutch_opus.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch126 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch126",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_french_opus.tar.gz -O $openslr_data_dir/SLR94/mls_french_opus.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch127 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch127",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_spanish_opus.tar.gz -O $openslr_data_dir/SLR94/mls_spanish_opus.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch128 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch128",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_italian_opus.tar.gz -O $openslr_data_dir/SLR94/mls_italian_opus.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/mls_portuguese_opus.tar.gz -O $openslr_data_dir/SLR94/mls_portuguese_opus.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/mls_polish_opus.tar.gz -O $openslr_data_dir/SLR94/mls_polish_opus.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch129 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch129",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_lm_english.tar.gz -O $openslr_data_dir/SLR94/mls_lm_english.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch130 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch130",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_lm_german.tar.gz -O $openslr_data_dir/SLR94/mls_lm_german.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/mls_lm_dutch.tar.gz -O $openslr_data_dir/SLR94/mls_lm_dutch.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/mls_lm_french.tar.gz -O $openslr_data_dir/SLR94/mls_lm_french.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/mls_lm_spanish.tar.gz -O $openslr_data_dir/SLR94/mls_lm_spanish.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/mls_lm_italian.tar.gz -O $openslr_data_dir/SLR94/mls_lm_italian.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch131 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch131",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_lm_portuguese.tar.gz -O $openslr_data_dir/SLR94/mls_lm_portuguese.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/mls_lm_polish.tar.gz -O $openslr_data_dir/SLR94/mls_lm_polish.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/lv_text.tar.gz -O $openslr_data_dir/SLR94/lv_text.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/unrated_transcripts.tar.gz -O $openslr_data_dir/SLR94/unrated_transcripts.tar.gz\nwget https://dl.fbaipublicfiles.com/mls/md5sum.txt -O $openslr_data_dir/SLR94/md5sum.txt\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch132 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch132",
        bash_command="wget https://www.openslr.org/resources/68/train_set.tar.gz -O $openslr_data_dir/SLR68/train_set.tar.gz\n",
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch133 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch133",
        bash_command="wget https://www.openslr.org/resources/51/TEDLIUM_release-3.tgz -O $openslr_data_dir/SLR51/TEDLIUM_release-3.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch134 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch134",
        bash_command="wget https://speech-lab-share-data.oss-cn-shanghai.aliyuncs.com/AliMeeting/openlr/Train_Ali_far.tar.gz -O $openslr_data_dir/SLR119/Train_Ali_far.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch135 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch135",
        bash_command="wget https://www.openslr.org/resources/89/Yoloxochitl-Mixtec-Data.tgz -O $openslr_data_dir/SLR89/Yoloxochitl-Mixtec-Data.tgz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch136 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch136",
        bash_command="wget https://www.openslr.org/resources/12/original-mp3.tar.gz -O $openslr_data_dir/SLR12/original-mp3.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    # upload openslr data to GCS
    upload_openslr_data_to_gcs_batch137 = bash.BashOperator(
        task_id="upload_openslr_data_to_gcs_batch137",
        bash_command="wget https://dl.fbaipublicfiles.com/mls/mls_english_opus.tar.gz -O $openslr_data_dir/SLR94/mls_english_opus.tar.gz\n",
        env={"openslr_data_dir": "/home/airflow/gcs/data/openslr/openslr"},
    )

    (
        create_folder
        >> upload_openslr_data_to_gcs_batch1
        >> upload_openslr_data_to_gcs_batch2
        >> upload_openslr_data_to_gcs_batch3
        >> upload_openslr_data_to_gcs_batch4
        >> upload_openslr_data_to_gcs_batch5
        >> upload_openslr_data_to_gcs_batch6
        >> upload_openslr_data_to_gcs_batch7
        >> upload_openslr_data_to_gcs_batch8
        >> upload_openslr_data_to_gcs_batch9
        >> upload_openslr_data_to_gcs_batch10
        >> upload_openslr_data_to_gcs_batch11
        >> upload_openslr_data_to_gcs_batch12
        >> upload_openslr_data_to_gcs_batch13
        >> upload_openslr_data_to_gcs_batch14
        >> upload_openslr_data_to_gcs_batch15
        >> upload_openslr_data_to_gcs_batch16
        >> upload_openslr_data_to_gcs_batch17
        >> upload_openslr_data_to_gcs_batch18
        >> upload_openslr_data_to_gcs_batch19
        >> upload_openslr_data_to_gcs_batch20
        >> upload_openslr_data_to_gcs_batch21
        >> upload_openslr_data_to_gcs_batch22
        >> upload_openslr_data_to_gcs_batch23
        >> upload_openslr_data_to_gcs_batch24
        >> upload_openslr_data_to_gcs_batch25
        >> upload_openslr_data_to_gcs_batch26
        >> upload_openslr_data_to_gcs_batch27
        >> upload_openslr_data_to_gcs_batch28
        >> upload_openslr_data_to_gcs_batch29
        >> upload_openslr_data_to_gcs_batch30
        >> upload_openslr_data_to_gcs_batch31
        >> upload_openslr_data_to_gcs_batch32
        >> upload_openslr_data_to_gcs_batch33
        >> upload_openslr_data_to_gcs_batch34
        >> upload_openslr_data_to_gcs_batch35
        >> upload_openslr_data_to_gcs_batch36
        >> upload_openslr_data_to_gcs_batch37
        >> upload_openslr_data_to_gcs_batch38
        >> upload_openslr_data_to_gcs_batch39
        >> upload_openslr_data_to_gcs_batch40
        >> upload_openslr_data_to_gcs_batch41
        >> upload_openslr_data_to_gcs_batch42
        >> upload_openslr_data_to_gcs_batch43
        >> upload_openslr_data_to_gcs_batch44
        >> upload_openslr_data_to_gcs_batch45
        >> upload_openslr_data_to_gcs_batch46
        >> upload_openslr_data_to_gcs_batch47
        >> upload_openslr_data_to_gcs_batch48
        >> upload_openslr_data_to_gcs_batch49
        >> upload_openslr_data_to_gcs_batch50
        >> upload_openslr_data_to_gcs_batch51
        >> upload_openslr_data_to_gcs_batch52
        >> upload_openslr_data_to_gcs_batch53
        >> upload_openslr_data_to_gcs_batch54
        >> upload_openslr_data_to_gcs_batch55
        >> upload_openslr_data_to_gcs_batch56
        >> upload_openslr_data_to_gcs_batch57
        >> upload_openslr_data_to_gcs_batch58
        >> upload_openslr_data_to_gcs_batch59
        >> upload_openslr_data_to_gcs_batch60
        >> upload_openslr_data_to_gcs_batch61
        >> upload_openslr_data_to_gcs_batch62
        >> upload_openslr_data_to_gcs_batch63
        >> upload_openslr_data_to_gcs_batch64
        >> upload_openslr_data_to_gcs_batch65
        >> upload_openslr_data_to_gcs_batch66
        >> upload_openslr_data_to_gcs_batch67
        >> upload_openslr_data_to_gcs_batch68
        >> upload_openslr_data_to_gcs_batch69
        >> upload_openslr_data_to_gcs_batch70
        >> upload_openslr_data_to_gcs_batch71
        >> upload_openslr_data_to_gcs_batch72
        >> upload_openslr_data_to_gcs_batch73
        >> upload_openslr_data_to_gcs_batch74
        >> upload_openslr_data_to_gcs_batch75
        >> upload_openslr_data_to_gcs_batch76
        >> upload_openslr_data_to_gcs_batch77
        >> upload_openslr_data_to_gcs_batch78
        >> upload_openslr_data_to_gcs_batch79
        >> upload_openslr_data_to_gcs_batch80
        >> upload_openslr_data_to_gcs_batch81
        >> upload_openslr_data_to_gcs_batch82
        >> upload_openslr_data_to_gcs_batch83
        >> upload_openslr_data_to_gcs_batch84
        >> upload_openslr_data_to_gcs_batch85
        >> upload_openslr_data_to_gcs_batch86
        >> upload_openslr_data_to_gcs_batch87
        >> upload_openslr_data_to_gcs_batch88
        >> upload_openslr_data_to_gcs_batch89
        >> upload_openslr_data_to_gcs_batch90
        >> upload_openslr_data_to_gcs_batch91
        >> upload_openslr_data_to_gcs_batch92
        >> upload_openslr_data_to_gcs_batch93
        >> upload_openslr_data_to_gcs_batch94
        >> upload_openslr_data_to_gcs_batch95
        >> upload_openslr_data_to_gcs_batch96
        >> upload_openslr_data_to_gcs_batch97
        >> upload_openslr_data_to_gcs_batch98
        >> upload_openslr_data_to_gcs_batch99
        >> upload_openslr_data_to_gcs_batch100
        >> upload_openslr_data_to_gcs_batch101
        >> upload_openslr_data_to_gcs_batch102
        >> upload_openslr_data_to_gcs_batch103
        >> upload_openslr_data_to_gcs_batch104
        >> upload_openslr_data_to_gcs_batch105
        >> upload_openslr_data_to_gcs_batch106
        >> upload_openslr_data_to_gcs_batch107
        >> upload_openslr_data_to_gcs_batch108
        >> upload_openslr_data_to_gcs_batch109
        >> upload_openslr_data_to_gcs_batch110
        >> upload_openslr_data_to_gcs_batch111
        >> upload_openslr_data_to_gcs_batch112
        >> upload_openslr_data_to_gcs_batch113
        >> upload_openslr_data_to_gcs_batch114
        >> upload_openslr_data_to_gcs_batch115
        >> upload_openslr_data_to_gcs_batch116
        >> upload_openslr_data_to_gcs_batch117
        >> upload_openslr_data_to_gcs_batch118
        >> upload_openslr_data_to_gcs_batch119
        >> upload_openslr_data_to_gcs_batch120
        >> upload_openslr_data_to_gcs_batch121
        >> upload_openslr_data_to_gcs_batch122
        >> upload_openslr_data_to_gcs_batch123
        >> upload_openslr_data_to_gcs_batch124
        >> upload_openslr_data_to_gcs_batch125
        >> upload_openslr_data_to_gcs_batch126
        >> upload_openslr_data_to_gcs_batch127
        >> upload_openslr_data_to_gcs_batch128
        >> upload_openslr_data_to_gcs_batch129
        >> upload_openslr_data_to_gcs_batch130
        >> upload_openslr_data_to_gcs_batch131
        >> upload_openslr_data_to_gcs_batch132
        >> upload_openslr_data_to_gcs_batch133
        >> upload_openslr_data_to_gcs_batch134
        >> upload_openslr_data_to_gcs_batch135
        >> upload_openslr_data_to_gcs_batch136
        >> upload_openslr_data_to_gcs_batch137
    )
