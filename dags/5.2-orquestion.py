from airflow import DAG
from airflow.operators.empty import EmptyOperator 
from datetime import datetime

with DAG(dag_id="5.2-Orquestacion",
         description="Probando orquestacion",
         schedule_interval= "0 7 * * 1",
         start_date=datetime(2025, 3, 2),
         end_date=datetime(2025, 4, 7),
         default_args= {"depends_on_past": True}) as dag:
    
    t1 = EmptyOperator(task_id ="tarea1")
    
    t2 = EmptyOperator(task_id ="tarea2")
    
    t3 = EmptyOperator(task_id ="tarea3")
    
    t4 = EmptyOperator(task_id ="tarea4")
    
    t1 >> t2 >>[t3,t4]