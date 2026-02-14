import pandas as pd

df=pd.read_csv("data/sales_raw.csv")

#handling missing values
df['amount']=df['amount'].fillna(df['amount'].mean())

#Remove dupicates
df=df.drop_duplicates()

df.to_csv("data/sales_cleaned.csv",index=False)

print("Data cleaning performed")

