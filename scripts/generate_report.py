import pandas as pd

df=pd.read_csv("data/sales_cleaned.csv")
summary=df.groupby("region")["amount"].sum()
summary.to_csv("data/sales_summary.csv")
print("Report generated successfully")


import matplotlib.pyplot as plt
summary.plot(kind='bar')
plt.title("Region-wise Sales")
plt.savefig("data/sales_plot.png")
