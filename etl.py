import pandas as pd
from sqlalchemy import create_engine

# 1. EXTRACT: Read the raw CSV file into a Pandas DataFrame (a digital table)
df = pd.read_csv('legacy_sales_data.csv')
print(f"Original row count: {len(df)}")

# 2. TRANSFORM: Clean the data
# - Remove duplicate rows based on Transaction ID
df = df.drop_duplicates(subset=['Transaction_ID'])

# - Fill missing email fields with 'N/A'
df['Email'] = df['Email'].fillna('N/A')

# - Standardize all date formats to YYYY-MM-DD
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'], format='mixed').dt.strftime('%Y-%m-%d')

print(f"Cleaned row count: {len(df)}")

# 3. LOAD: Connect to the database and save the clean table
# Using SQLite for a smooth setup (creates a file named 'ci_db.db' locally)
engine = create_engine('sqlite:///ci_db.db')

# If you prefer PostgreSQL as noted in your resume, use this line instead:
# engine = create_engine('postgresql://username:password@localhost:5432/ci_db')

df.to_sql('migrated_sales', engine, if_exists='replace', index=False)

print("ETL Pipeline executed successfully!")