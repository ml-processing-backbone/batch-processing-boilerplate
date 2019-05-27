# product-analytics


## How to Run
1. Installation in GCP UI
    1. Create Cloud Composer cluster via GCP UI
       - Define connections via UI
    2. Go to Cloud Dataflow UI and enable APIs via GCP UI

2. Install GCP SDK on your local
3. Install anaconda via `brew cask install anaconda` and 
    1. Create environment w/ 
        - `conda create -n airflow-sandbox python=3.7 anaconda`
        - `conda activate airflow-sandbox`
    
    2. Install airflow packages 
       - `pip install  apache-airflow[async,crypto,jdbc,gcp_api,google_auth]`
4. Additional installations on Cloud Composer Workers ?
5. `git clone https://github.com/tansudasli/airflow-sandbox.git`
6. `cd /airflow-sandbox/product-analytics`
7. Run `./prepare-environment.sh`
