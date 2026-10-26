import pandas as pd
from sqlalchemy import create_engine

# Connect to your local SQLite database file
engine = create_engine('sqlite:///ci_db.db')

print("Running SQL Validation Queries...\n")

# 1. Check total row count to ensure data loaded properly
total_rows_df = pd.read_sql("SELECT COUNT(*) AS total_rows FROM migrated_sales;", engine)
print("1. Total Row Count:")
print(total_rows_df.to_string(index=False))
print("\n" + "-"*40 + "\n")

# 2. Check for any remaining duplicates (should return 0 rows)
duplicates_df = pd.read_sql("""
    SELECT transaction_id, COUNT(*) as count 
    FROM migrated_sales 
    GROUP BY transaction_id 
    HAVING COUNT(*) > 1;
""", engine)

print("2. Duplicate Check Results (If empty below, your data is clean!):")
if duplicates_df.empty:
    print("SUCCESS: Zero duplicates found! Data integrity verified.")
else:
    print(duplicates_df)