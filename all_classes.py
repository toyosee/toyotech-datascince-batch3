import sqlite3 as sql3
import pandas as pd
import os

# print(sql3.sqlite_version)  

if not os.path.exists("data/processed_data"):
    os.makedirs("data/processed_data")
    
db_path = "data/processed_data/db_analytics.db"
conn = sql3.connect(db_path)

# df = pd.DataFrame()
# # A new test is here

# def greet(name):
#     return f"Hello, {name}!"

orders = pd.read_csv("data/raw/orders.csv")
customers = pd.read_csv("data/raw/customers.csv")

# print(orders.head())

orders.to_sql("orders", conn, if_exists="replace", index=False)
customers.to_sql("customers", conn, if_exists="replace", index=False)

# query = """
# SELECT * FROM orders
# ORDER BY order_id DESC
# LIMIT 5;
# """

query = """
SELECT 
c.customer_id, c.signup_channel, c.loyalty_tier, c.region,
o.order_date, o.amount 
FROM customers c
JOIN orders o 
ON c.customer_id = o.customer_id
ORDER BY o.amount DESC;
"""

# all_customers = pd.read_sql_query(query, conn)
last_5_orders = pd.read_sql_query(query, conn)
customers_and_orders = pd.read_sql_query(query, conn)
print(customers_and_orders.head())