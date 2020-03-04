# product-analytics


## How to Run

1. CLI configurations
   1. Install GCP SDK on your local
   2. Install anaconda via `brew cask install anaconda` and 
    1. Create environment w/ 
        - `conda create -n airflow-sandbox python=3.7 anaconda`
        - `conda activate airflow-sandbox`
    
    2. Install airflow packages 
       - `pip install  apache-airflow[async,crypto,jdbc,gcp_api,google_auth]`

2. Create a GCP project via GCP console and enable APIs (composer, dataflow, storage etc) on GCP console
3. Create airflow environment <br>
`gcloud composer environments create airflow-cluster \
                             --location europe-west1 \
                             --image-version composer-1.7.0-airflow-1.10.2 \
                             --python-version 3 \
                             --env-variables=INGESTION_BUCKET_NAME=datalake-datasets-123,\
                                             BEAM_BUCKET_NAME=beam-pipelines-123,\
                                             AVERAGE_PRICES_BY_PRODUCT_ENHANCED_FILE_NAME=average-prices-by-product-enhanced \
                             --disk-size=30GB \
                             --async`

3. `git clone https://github.com/tansudasli/airflow-sandbox.git`
4. `cd /airflow-sandbox/product-analytics`
5. Edit `prepare-environment.sh` and set env. variables, then Run `./prepare-environment.sh`
6. Define airflow connections via airflow UI

