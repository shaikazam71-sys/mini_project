import pandas as pd

from sqlalchemy import create_engine, text

# 'Dell@123' me '@' ko '%40' likha hai URL encoding ke liye
engine = create_engine("mysql+pymysql://root:Dell%6666@localhost/expense_analytics")

try:
    with engine.connect() as connection:
        print("Connected to MySQL database successfully!")

        # Query run karke top 5 rows retrieve karna
        result = connection.execute(text("SELECT * FROM transactions LIMIT 5"))

        print("\n--- Query Results ---")
        for row in result:
            print(row)

except Exception as e:
    print(f"Error: {e}")

print("\nMySQL connection closed.")
query = "SELECT * FROM transactions"

df = pd.read_sql(query, engine)

print(df.head())
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
print(df.dtypes)
print(df.describe())
df['transaction_type'] = df['transaction_type'].str.strip("'")

expenses = df[df['transaction_type'] == 'Expense']
print(expenses.shape)

print(expenses['amount'].sum())

category_expense = expenses.groupby('category')['amount'].sum()
print(category_expense)
monthly_expense = expenses.groupby(
    expenses['transaction_date'].dt.to_period('M')
)['amount'].sum()

print(monthly_expense)
payment_expense = expenses.groupby('payment_method')['amount'].sum()

print(payment_expense)
# Income, Expense & Savings
total_income = df[df['transaction_type'] == 'Income']['amount'].sum()
total_expense = expenses['amount'].sum()

savings = total_income - total_expense

print("Total Income:", total_income)
print("Total Expense:", total_expense)
print("Savings:", savings)
df.to_csv("expense_transactions.csv", index=False)
print("CSV file created successfully!")
