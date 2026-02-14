import sqlite3
import pandas as pd
#connect to db
conn=sqlite3.connect("database/sales.db")

#sql query
query="""
SELECT region, SUM(amount) AS
 total_sales
 FROM sales
 GROUP BY region
"""

df= pd.read_sql_query(query,conn)
#Save sql summary
df.to_csv("data/sql_sales_summary.csv",index=False)

conn.close()
print("SQL analysis completed successfully")
