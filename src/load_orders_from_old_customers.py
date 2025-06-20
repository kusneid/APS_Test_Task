import pandas as pd
from sqlalchemy import create_engine
from src.config import Config

engine = create_engine(Config.db_uri)

def load_orders_from_old_customers(path: str):
    df = pd.read_csv(path, parse_dates=['order_date'])  # читаем новые заказы
    cust = pd.read_sql_table('customers', engine, columns=['customer_id'])
    df = df[df['customer_id'].isin(cust['customer_id'])]  # фильтруем по существующим клиентам
    df.to_sql('orders', engine, if_exists='append', index=False)  # пишем в orders