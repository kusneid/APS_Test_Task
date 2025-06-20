import pandas as pd
from sqlalchemy import create_engine
from src.config import Config

engine = create_engine(Config.db_uri)

def load_cleared_order_items(path: str):
    df = pd.read_csv(path)  # читаем новые позиции
    ords = pd.read_sql_table('orders', engine, columns=['order_id'])
    df = df[df['order_id'].isin(ords['order_id'])]  # фильтруем по существующим заказам
    pr = pd.read_sql_table('products', engine, columns=['product_id', 'price'])
    df = df[df['product_id'].isin(pr['product_id'])]  # проверяем продукты
    df = df.merge(pr, on='product_id', how='left').rename(columns={'price': 'unit_price'})
    df.to_sql('order_items', engine, if_exists='append', index=False)  # записываем в order_items