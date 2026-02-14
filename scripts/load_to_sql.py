import pandas as pd
import sqlite3

#connect to db
conn=sqlite3.connect("database/sales.db")
#load cleaned data
df=pd.read_csv("data/sales_cleaned.csv")

#write sql table
df.to_sql("sales",conn,if_exists="replace",index=False)

conn.commit()
conn.close()

print("Data loaded into SQLite database successfully")
