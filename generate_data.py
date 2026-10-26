import random
import pandas as pd
from datetime import datetime, timedelta

# Create 5,000 rows of fake legacy sales data with intentional messiness
data = []
start_date = datetime(2023, 1, 1)

for i in range(1, 5001):
    # FIXED: Removed the extra closing curly brace
    trans_id = f"TXN-{random.randint(1000, 1500)}" 
    cust_id = f"CUST-{random.randint(100, 500)}"
    
    # Inconsistent date formats (MM/DD/YYYY vs YYYY-MM-DD)
    rand_days = random.randint(0, 700)
    dt = start_date + timedelta(days=rand_days)
    date_str = dt.strftime('%m/%d/%Y') if i % 2 == 0 else dt.strftime('%Y-%m-%d')
    
    # Missing email fields for some rows
    email = f"client_{i}@example.com" if i % 10 != 0 else None
    
    amount = round(random.uniform(50.5, 5000.0), 2)
    
    data.append({
        'Transaction_ID': trans_id,
        'Customer_ID': cust_id,
        'Transaction_Date': date_str,
        'Email': email,
        'Amount': amount
    })

df = pd.DataFrame(data)
df.to_csv('legacy_sales_data.csv', index=False)
print("legacy_sales_data.csv generated successfully with 5,000 rows!")