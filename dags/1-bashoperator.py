from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(dag_id="bashoperator",
         description="utilizando bash operator",
         start_date=datetime(2025, 4, 1)         
         ) as dag:
    t1 = BashOperator(task_id="hello_with_bash",
                      bash_command="echo 'Hello platzi'")
    t1
    