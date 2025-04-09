from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime, date
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator

default_args = {
    'start_date' : datetime(2025, 3, 1),
    'end_date' : datetime(2025, 4, 3)
}

def _choose(**context):
    if context["logical_date"].date() < date(2025, 3, 25):
        return "finishA"
    return "finishB"

with DAG(dag_id="10-branching",
         description="Probando los branching",
         schedule_interval="@daily",
         default_args = default_args) as dag:
    
    branching = BranchPythonOperator(task_id="branch",
                                     python_callable= _choose)
                                     
    finishA = BashOperator(task_id="finishA",
                          bash_command = "echo 'Running {{ds}}'")
    
    finisthB = BashOperator(task_id="finishB",
                          bash_command = "echo 'Running {{ds}}'")
    
    
    branching >> [finishA, finisthB]