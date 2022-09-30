from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime, timedelta

with DAG(
        dag_id="dag_two",
        start_date=datetime(2021, 1, 1),
        catchup=False,
        schedule_interval=None,
) as dag:
    dag_two_task1 = BashOperator(
        task_id="dag_two_task1",
        bash_command=f"echo Hello from Dag Two"
    )

    dag_two_task2 = BashOperator(
        task_id="dag_two_task2",
        bash_command=f"echo We have finished"
    )

    dag_two_task1 >> dag_two_task2
