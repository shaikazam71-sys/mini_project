# Personal Expense Analytics & Data Pipeline

A mini project for processing and analyzing personal expense transaction data using Python, Pandas, MySQL, SQL, and Power BI.

## 📌 Project Overview

This project implements a simple data pipeline for personal expense analytics.

Transaction data is stored in MySQL. Python and Pandas are used to extract, clean, and transform the data. The processed data is exported to a CSV file, which is connected to Power BI for interactive analysis and visualization.

## 🔄 Data Pipeline

MySQL Database
↓
Python + Pandas
↓
Data Cleaning & Feature Engineering
↓
Processed CSV
↓
Power BI Dashboard
↓
Financial Insights

## ✨ Features

- **Database Integration:** Connected Python to MySQL to retrieve transaction data.
- **Data Cleaning:** Standardized dates, categories, and merchant names.
- **Feature Engineering:** Created Year-Month, Day Name, and Weekday/Weekend fields.
- **Data Processing:** Used Pandas for filtering, grouping, and financial analysis.
- **Automated Pipeline:** Running the Python ETL script fetches the latest data from MySQL and updates the processed CSV.
- **Interactive Dashboard:** Power BI displays income, expenses, savings, monthly trends, categories, payment methods, and top expense merchants.

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, SQLAlchemy
- **Database:** MySQL
- **Query Language:** SQL
- **Data Format:** CSV
- **Visualization:** Power BI

## 📊 Dashboard

The Power BI dashboard provides:

- Total Income
- Total Expense
- Savings
- Savings Percentage
- Monthly Income vs Expenses
- Expenses by Category
- Expenses by Payment Method
- Top 5 Expense Merchants
- Interactive Filters

## ⚙️ How the Pipeline Works

1. Transaction data is stored in MySQL.
2. Python connects to MySQL and retrieves the latest transaction data.
3. Pandas cleans and transforms the data.
4. Additional analytical fields are created.
5. The processed dataset is exported to a CSV file.
6. Power BI reads the updated CSV.
7. After refreshing Power BI, the dashboard reflects the latest transaction data.

## 🎯 Project Objective

The objective of this project is to demonstrate how raw financial transaction data can be processed through a simple ETL pipeline and converted into meaningful financial insights using data analytics tools.
