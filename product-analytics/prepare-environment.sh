#!/usr/bin/env bash

echo "edit env variables "
echo "install airflow-cluster and enable dataflow apis etc.."
echo "run scripts inside product-analytics folder !!"

export GCP_PROJECT_NAME=sandbox-236618

export BEAM_BUCKET_NAME=beam-pipelines-123
export BEAM_FILE_NAME=average-prices-by-product-enhanced

export INGESTION_BUCKET_NAME=sandbox-datalake-123

export AIRFLOW_BUCKET_NAME=europe-west1-airflow-cluste-0bf08843-bucket


echo "***** create buckets for ingestion"
gsutil mb -b on gs://${INGESTION_BUCKET_NAME}

# ${BUCKET_NAME}/incoming
# ${BUCKET_NAME}/datalake
# ${BUCKET_NAME}/processing

echo "***** transfer DAG file into airflow"
gsutil cp product-analytics/product-analytics-DAG.py gs://${AIRFLOW_BUCKET_NAME}/dags



# -------------------------------  simulation -------------------------
echo "simulate ingestion of input files instead of SFTP thing"


echo "***** transfer files for ingestion"

for FILE_SUFFIX in 001 002 003 004 005
do
   gsutil cp ./dataset/sales_transactions_${FILE_SUFFIX}.csv gs://${INGESTION_BUCKET_NAME}

   sleep 1m

done



