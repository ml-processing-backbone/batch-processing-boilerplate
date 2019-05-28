

from airflow import DAG
from airflow.contrib.sensors.gcs_sensor import GoogleCloudStoragePrefixSensor
from airflow.contrib.operators.gcs_to_gcs import GoogleCloudStorageToGoogleCloudStorageOperator
from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator

from datetime import datetime, timedelta

#
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 5, 28),
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

PROJECT = "sandbox-236618"
REGION = "europe-west1"
ZONE = "europe-west1-a"
INGESTION_BUCKET_NAME = "datalake-datasets-123"
BEAM_BUCKET_NAME = "beam-pipelines-123"
AVERAGE_PRICES_BY_PRODUCT_ENHANCED_FILE_NAME = "average-prices-by-product-enhanced"

with DAG('product-analytics', default_args=default_args, schedule_interval=timedelta(seconds=10)) as dag:

    # TODO: not implemented
    # listen customers FTP server folder w/ sensor
    # define sftp-default connection in Airflow UI
    # t1 = SFTPSensor(
    #     task_id='listen-sftp-server',
    # )

    # TODO: not implemented
    # copy from sftp to gcp storage's incoming folder
    # scenario will start right from here !
    # t2 = SFTPOperator(
    #     task_id='transfer-to-incoming',
    # )

    # Listen incoming folder w/ sensor
    t3 = GoogleCloudStoragePrefixSensor(
        task_id='listen-incoming-file',
        bucket='datalake-datasets-123',
        prefix='incoming/sales_transactions_*'
    )

    # TODO: better file structure can be defined, such as monthly aggregation datalake/sales/05/sales_transactions_*
    # copy from gcs to datalake for raw data storing
    t4 = GoogleCloudStorageToGoogleCloudStorageOperator(
        task_id='copy-to-datalake',
        source_bucket=INGESTION_BUCKET_NAME,
        source_object='incoming/sales_transactions_*',
        destination_bucket=INGESTION_BUCKET_NAME,
        destination_object='datalake/sales_transactions_',
        move_object=False
    )

    # copy from gcs to process for analytical calculations
    t5 = GoogleCloudStorageToGoogleCloudStorageOperator(
        task_id='move-to-processing',
        source_bucket=INGESTION_BUCKET_NAME,
        source_object='incoming/sales_transactions_*',
        destination_bucket=INGESTION_BUCKET_NAME,
        destination_object='processing/sales_transactions_',
        move_object=True
    )

    # git clone average-prices-by-product-enhanced.py file ?????
    # deploy to GCP dataflow as a beam job, and check GCP dataflow job status
    options = {'autoscalingAlgorithm': 'NONE',
               'maxNumWorkers': '2'}
    dataflow_default_options = {
        'project': PROJECT,
        'region': REGION,
        'stagingLocation': 'gs://' + BEAM_BUCKET_NAME + "/" + AVERAGE_PRICES_BY_PRODUCT_ENHANCED_FILE_NAME + '/staging',
        'tempLocation': 'gs://' + BEAM_BUCKET_NAME + "/" + AVERAGE_PRICES_BY_PRODUCT_ENHANCED_FILE_NAME + '/temp'}
    t6 = DataFlowPythonOperator(
        task_id='deploy-averages-prices-by-product-job',
        options=options,
        dataflow_default_options=dataflow_default_options,
        job_name=AVERAGE_PRICES_BY_PRODUCT_ENHANCED_FILE_NAME,
        py_file='/home/airflow/gcs/data/average-prices-by-product-enhanced.py'
    )

    t4 >> t3
    t5 >> t3
    t6 >> t3


