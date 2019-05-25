import logging

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.sftp_sensor import SFTPSensor
from airflow.contrib.sensors.gcs_sensor import GoogleCloudStorageObjectSensor
from airflow.contrib.operators.sftp_operator import SFTPOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator
from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator
from airflow.contrib.operators.gcs_to_gcs import GoogleCloudStorageToGoogleCloudStorageOperator
from datetime import datetime, timedelta

#
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email': ['tansudasli@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

with DAG('product-analytics', default_args=default_args, schedule_interval=timedelta(minutes=10)) as dag:

    # TODO: not implemented for now
    # listen customers FTP server folder w/ sensor
    # define sftp-default connection in Airflow UI
    t1 = SFTPSensor(
        task_id='listen-sftp-server',
        bash_command=''
    )

    # TODO: not implemented for now
    # copy from sftp to gcp storage
    t2 = SFTPOperator(
        task_id='transfer-to-datalake',
        bash_command=''
    )

    # copy from gcs to process bucket for analytical calculations
    t3 = GoogleCloudStorageToGoogleCloudStorageOperator(
        task_id='copy-for-analytics',
        bash_command=''
    )

    # git clone average-prices-by-product-enhanced.py file ?????
    # deploy to GCP dataflow as a beam job, and check GCP dataflow job status
    t4 = DataFlowPythonOperator(
        task_id='copy-for-analytics',
        bash_command=''
    )

    # Listen output folder w/ sensor
    t5 = GoogleCloudStorageObjectSensor(
        task_id='copy-for-analytics',
        bash_command=''
    )
    # transfer output file to SFTP server
    t6 = SFTPOperator(
        task_id='transfer-to-datalake',
        bash_command=''
    )

    t3 >> t2 >> t1

