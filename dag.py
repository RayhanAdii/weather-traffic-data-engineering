
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 15, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'run_main_every_15_minutes',
    default_args=default_args,
    schedule_interval=timedelta(minutes=15),
)

run_main = BashOperator(
    task_id='run_main',
    bash_command='python3 /home/rayhan_adi_wicaksono/rekdat-traffic-weather/weather-traffic-data-engineering/Main.py',
    dag=dag,
)
