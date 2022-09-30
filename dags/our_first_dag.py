from datetime import datetime
from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(
        dag_id="dag_one",
        start_date=datetime(2021, 1, 1),
        catchup=False,
        schedule_interval=None,
) as dag:
    test_trigger_dagrun = TriggerDagRunOperator(
        task_id="test_trigger_dagrun",
        trigger_dag_id="dag_two",  # Ensure this equals the dag_id of the DAG to trigger
    )
