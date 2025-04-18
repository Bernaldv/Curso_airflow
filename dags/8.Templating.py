from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime

template_command = """
{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "{{ file }}"
{% endfor %}
"""

with DAG(dag_id="8Templating",
         description="DAG de ejemplo para templating",
         schedule_interval="@daily",
         start_date=datetime(2025, 3, 1),
         end_date=datetime(2025, 4, 3),
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id="tarea1",
                      bash_command=template_command,
                      params= {"filenames":["file1.txt", "file2.txt"]},
                      depends_on_past=True
    
)
    t1