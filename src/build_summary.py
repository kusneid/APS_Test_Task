import pandas as pd
from sqlalchemy import create_engine
from src.config import Config

engine = create_engine(Config.db_uri)

def build_customer_summary():
    orders = pd.read_sql_table('orders', engine, parse_dates=['order_date'])
    items  = pd.read_sql_table('order_items', engine)
    cust   = pd.read_sql_table('customers', engine)

    # считаем число заказов и дату последнего
    order_agg = orders.groupby('customer_id').agg(
        total_orders    = ('order_id', 'nunique'),
        last_order_date = ('order_date', 'max')
    )

    # считаем траты по позициям
    spent = (
        items
        .merge(orders[['order_id', 'customer_id']], on='order_id')
        .assign(line_total=lambda df: df.quantity * df.unit_price)
        .groupby('customer_id')['line_total']
        .sum()
        .rename('total_spent')
    )

    # объединяем по индексу customer_id
    summary = (
        cust.set_index('customer_id')
        .join(order_agg)
        .join(spent)
        .fillna({'total_orders': 0, 'total_spent': 0})
    )
    summary['total_orders'] = summary['total_orders'].astype(int)

    return summary
