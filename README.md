# Automated Sales Data Cleaning & Reporting Pipeline (Linux-Based)

A Linux-based automated data processing pipeline built using Python and Bash to simulate real-world ETL workflows.

---

## 📌 Project Overview

This project simulates a real-world scenario where raw CSV sales data is received daily and needs to be:

- Cleaned
- Processed
- Summarized
- Logged
- Automated using shell scripting

## 🛠️ Tech Stack
- Ubuntu (WSL)
- Python 3
- Pandas
- Matplotlib
- Shell Scripting (Bash)
- Virtual Environment
- Git

## 📂 Project Structure
sales_pipeline/
│
├── data/
│   ├── sales_raw.csv
│   ├── sales_cleaned.csv
│   └── sales_summary.csv
│
├── scripts/
│   ├── clean_data.py
│   └── generate_report.py
│
├── logs/
│   └── pipeline.log
│
├── run_pipeline.sh
├── requirements.txt
└── README.md

## 🔄 Pipeline Workflow

1. Read raw CSV data
2. Handle missing values
3. Remove duplicates
4. Generate region-wise sales summary
5. Log execution details
6. Automate entire workflow using shell script

## ▶️ How to Run

Activate virtual environment:
```bash
source venv/bin/activate
```
Run the pipeline

```bash
./run_pipeline.sh
```

## 📊 Output

- Cleaned dataset
- Region-wise sales summary
- Execution logs

---

## 🗄 SQL Integration

The pipeline integrates SQLite for database-level aggregation and analysis.

### Steps Performed:

1. Cleaned CSV data is loaded into a SQLite database.
2. SQL queries are executed to calculate region-wise total sales.
3. SQL output is exported as `sql_sales_summary.csv`.
4. Entire process is automated within the shell pipeline.

### Example SQL Query Used:

```sql
SELECT region, SUM(amount) AS total_sales
FROM sales
GROUP BY region;

## 🎯 Learning Outcomes

- Data preprocessing using Pandas
- Linux file management
- Shell scripting automation
- Logging and error handling
- Git version control


