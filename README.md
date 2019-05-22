# airflow-sandbox


### How To Start

1. Create environment w/ 
   - `conda create -n airflow-sandbox python=3.7 anaconda`
   - `conda activate airflow-sandbox`

2. Install airflow packages 
   - `pip install  apache-airflow[async,crypto,jdbc,gcp_api,google_auth]`

3. Start airflow on your local 
   - `airflow initdb`
   - `ls ~/airflow`
   - `mkdir ~/airflow/dags`
   - `airflow webserver -p 8080`
   - `airflow scheduler`
   - Open `localhost:8080` in your web browser
4. Copy dag files into dags folder like `cp basic-dag.py ~/airflow/dags`