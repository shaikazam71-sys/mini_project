import pandas as pd
from sqlalchemy import create_engine

# 1. Connect to MySQL and load raw data
engine = create_engine("mysql+pymysql://root:Dell%40123@localhost/expense_analytics")
query = "SELECT * FROM transactions;"
df = pd.read_sql(query, con=engine)

# 2. Perform Pandas Data Cleaning & Transformations
# Ensure correct datetime format
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Extract useful time features
df['year_month'] = df['transaction_date'].dt.strftime('%Y-%m')
df['day_name'] = df['transaction_date'].dt.day_name()
df['is_weekend'] = df['transaction_date'].dt.dayofweek.isin([5, 6]).map({True: 'Weekend', False: 'Weekday'})

# Clean text fields (remove leading/trailing whitespace)
df['merchant'] = df['merchant'].str.strip().str.title()
df['category'] = df['category'].str.strip().str.title()

# 3. Save the cleaned DataFrame to CSV
# Absolute path set kar do taaki same file overwrite ho
output_path = r"E:\python practice\pandas\mini-project\expense_transactions.csv"
df.to_csv(output_path, index=False)
print(f"Pipeline executed successfully! Cleaned data exported to {output_path}")