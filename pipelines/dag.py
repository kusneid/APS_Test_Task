from datetime import datetime
from airflow.decorators import dag
from airflow.operators.python import PythonOperator
from src.config import Config
from src.load_orders_from_old_customers import load_orders_from_old_customers
from src.load_cleared_order_items import load_cleared_order_items
from src.build_summary import build_customer_summary

@dag(
    schedule="@daily",
    start_date=datetime.now(),
    catchup=False
)
def etl_orders_pipeline():
    load_orders_task = PythonOperator(
        task_id="load_orders",
        python_callable=load_orders_from_old_customers,
        op_kwargs={"path": Config.orders_csv},
    )

    load_order_items_task = PythonOperator(
        task_id="load_order_items",
        python_callable=load_cleared_order_items,
        op_kwargs={"path": Config.order_items_csv},
    )

    build_summary_task = PythonOperator(
        task_id="build_summary",
        python_callable=build_customer_summary,
    )

    load_orders_task >> load_order_items_task >> build_summary_task

