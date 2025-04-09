from airflow import DAG
from airflow.operators.bash import BashOperator 
from datetime import datetime
from airflow.sensors.filesystem import FileSensor

with DAG(dag_id="7.3FileSensor",
         description="FileSensor",
         schedule_interval="@daily",
         start_date=datetime(2025,3,1),
         end_date=datetime(2025,4,3),
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id="creating_file",
                      bash_command="sleep 10 && touch /tmp/file.txt",
                    
    )
    #poke_interval  espera cada n segundos para ver si finalizo
    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/file.txt")
    
    
       #poke_interval  espera cada n segundos para ver si finalizo
    t3 = BashOperator(task_id="end_task",
                      bash_command="echo 'El fichero ha llegado'")
                               
    t1 >> t2 >> t3
    
