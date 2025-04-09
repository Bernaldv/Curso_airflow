from airflow import DAG
from airflow.operators.bash import BashOperator 
from airflow.operators.python import PythonOperator 
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule


def myfunction():
    raise Exception

default_args = {}

with DAG(dag_id="6.2-Monitoring",
         description="Monitoreando 2  DAG",
         schedule_interval= "@daily",
         start_date=datetime(2025, 3, 1),
         end_date=datetime(2025, 4, 7),
         default_args=default_args,
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id ="tarea1",
                      bash_command="sleep 2 && echo 'Primera tarea!'",
                      trigger_rule = TriggerRule.ALL_SUCCESS,
                      retries=2,
                      retry_delay=5
                      )
    #retries  indica la cantidad de intentos
    
    t2 = BashOperator(task_id ="tarea2",
                      bash_command="sleep 2 && echo 'Segunda tarea!'",
                      retries=2,
                      retry_delay=5,
                      trigger_rule=TriggerRule.ALL_SUCCESS)
    
    t3 = BashOperator(task_id ="tarea3",
                      bash_command="sleep 2 && echo 'Tercera tarea!'",
                      retries=2,
                      retry_delay=5,
                      trigger_rule=TriggerRule.ALWAYS)
    
    t4 = PythonOperator(task_id ="tarea4",
                        python_callable=myfunction,
                        retries=2,
                        retry_delay=5)
    
    t5 = BashOperator(task_id ="tarea5",
                      bash_command="sleep 2 && echo 'Quinta tarea!'")
    
    t1 >> t2 >> t3 >>t4 >> t5