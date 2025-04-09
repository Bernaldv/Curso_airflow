from airflow import DAG
from airflow.operators.empty import EmptyOperator 
from datetime import datetime

with DAG(dag_id="5.3-Orquestacion",
         description="Probando orquestacion 3",
         schedule_interval= "@monthly",
         start_date=datetime(2025, 2, 1),
         end_date=datetime(2025, 4, 7)) as dag:
    
    t1 = EmptyOperator(task_id ="tarea1")
    
    t2 = EmptyOperator(task_id ="tarea2")
    
    t3 = EmptyOperator(task_id ="tarea3")
    
    t4 = EmptyOperator(task_id ="tarea4")
    
    t1 >> t2 >>[t3,t4]