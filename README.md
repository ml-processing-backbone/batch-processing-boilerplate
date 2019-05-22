# airflow-sandbox

`conda create -n airflow-sandbox python=3.7 anaconda`
`conda activate airflow-sandbox`

`pip install  apache-airflow[async,crypto,jdbc,gcp_api,google_auth]`
`airflow initdb`

`ls ~/airflow`

airflow webserver -p 8080
airflow scheduler

cp /Users/tansudasli/Desktop/dag-examples/basic-dag.py airflow/dags