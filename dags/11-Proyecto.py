from airflow import DAG
from airflow.operators.bash import BashOperator 
from datetime import datetime
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from custom_operator import customer_operator

def _generate_data_satellite(**kwargs):
    import pandas as pd
    data = pd.DataFrame({"student": ["Maria Cruz", "Daniel Crema","Elon Musk", "Karol Castrejon", "Freddy Vega"],
                         "timestamp": [kwargs['logical_date'],kwargs['logical_date'], kwargs['logical_date'], kwargs['logical_date'],kwargs['logical_date']]})
    
    data.to_csv(f"/tmp/platzi_data_{kwargs['ds_nodash']}.csv",header=True)
 
default_args = {
    'owner': 'airflow', #Identificador de Ejecutor
    'email': ['vickyber7@gmail.com'], 
    'email_on_failure': True,  # Envio de Email en deteccion de fallas
    'email_on_retry': False, #Reintentos de Envios en caso de fallas
    'retries': 1  #Numero de reintentos
}

with DAG(dag_id="11.ExploraSpaceX",
         description="FileSensor",
         default_args=default_args,
         schedule_interval="@daily",
         start_date=datetime(2025,4,6),
         end_date=datetime(2025,4,9),
         max_active_runs=1,
         catchup = True) as dag:
    
    t1 = BashOperator(task_id="approval_file",
                      bash_command='sleep 20 && echo "OK" > /tmp/response_{{ds_nodash}}.txt'
                    
    )
    #poke_interval  espera cada n segundos para ver si finalizo
    t2 = FileSensor(task_id="waiting_approval_file_nasa",
                    filepath= 'response_{{ds_nodash}}.txt')
    
    
    t3 = BashOperator(task_id="collect_data_fromSpacex",
                      bash_command="curl -o /tmp/history.json -L 'https://api.spacexdata.com/v4/history'")
    
    t4 = PythonOperator(task_id="response_satellite",
                        python_callable=_generate_data_satellite)
    
        #Custom Task de Envio de Email
    email = customer_operator(
        task_id="enviar_correo",
        subject="Ejecución del DAG en la fecha {ds}",
        mensaje="Hola equipo,\n\nLa ejecución para el DAG del día {ds} ha sido completada exitosamente.\n\nSaludos.",
        to_email="vickyber7@gmail.com",
        conn_id="gmail_conn",  # Este es el ID de tu conexión SMTP en Airflow UI
    )

 
    t1 >> t2 >> t3 >> t4 >> email
    
