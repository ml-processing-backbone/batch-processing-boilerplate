#!/usr/bin/env bash

echo "edit env variables "
echo "install airflow-cluster and enable dataflow apis etc.."
echo "run scripts inside product-analytics folder !!"

export PROJECT_ID=sandbox-236618
export REGION=europe-west1
export ZONE=europe-west1-a

export BEAM_BUCKET_NAME=beam-pipelines-123
export AVERAGE_PRICES_BY_PRODUCT_ENHANCED_FILE_NAME=average-prices-by-product-enhanced

export INGESTION_BUCKET_NAME=datalake-datasets-123

export AIRFLOW_BUCKET_NAME=europe-west1-airflow-cluste-77117cb6-bucket  #get from gcs buckets and update


# -------------------------------  preparations -------------------------
echo "***** create ingestion buckets"
gsutil mb -b on gs://${INGESTION_BUCKET_NAME}

# ${BUCKET_NAME}/incoming
# ${BUCKET_NAME}/datalake
# ${BUCKET_NAME}/processing
# ${BUCKET_NAME}/output
# ${BUCKET_NAME}/processed

echo "***** create beam pipeline bucket"
gsutil mb -b on gs://${BEAM_BUCKET_NAME}


echo "***** transfer DAG file into airflow"
gsutil cp product-analytics-DAG.py gs://${AIRFLOW_BUCKET_NAME}/dags

gsutil cp average-prices-by-product-enhanced.py gs://${AIRFLOW_BUCKET_NAME}/plugins


# -------------------------------  simulation -------------------------
echo "simulate ingestion of input files instead of SFTP thing"


echo "***** transfer files for ingestion"

for FILE_SUFFIX in 001 002 003 004 005
do
   gsutil cp ./dataset/sales_transactions_${FILE_SUFFIX}.csv gs://${INGESTION_BUCKET_NAME}/incoming

   sleep 2m

done



