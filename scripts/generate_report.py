import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/sales_cleaned.csv")

# Generate summary
summary = df.groupby("region")["amount"].sum()

# Save summary CSV
summary.to_csv("data/sales_summary.csv")

# Create bar chart
plt.figure()
summary.plot(kind="bar")
plt.title("Region-wise Sales Summary")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("data/sales_chart.png")
plt.close()

print("Report generated successfully")
import pandas as pd

df=pd.read_csv("data/sales_cleaned.csv")
summary=df.groupby("region")["amount"].sum()
summary.to_csv("data/sales_summary.csv")
print("Report generated successfully")


import matplotlib.pyplot as plt
summary.plot(kind='bar')
plt.title("Region-wise Sales")
plt.savefig("data/sales_plot.png")
