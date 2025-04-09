from airflow import DAG
from datetime import datetime
from helloOperator import HelloOperator


with DAG(dag_id="CustumOperator",
         description="Mi primer customoperator",
         start_date=datetime(2025, 4, 2)) as dag:
    
    t1 = HelloOperator(task_id ="hello",
                       name="Fredy")
    t1
    
    