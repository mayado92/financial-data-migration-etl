# Financial Data Migration & SQL ETL Pipeline

## Overview
This project simulates a real-world financial data migration workflow for client and sales records. Legacy sales systems often store redundant, incomplete, or inconsistently formatted data. This automated Python ETL pipeline cleanses raw dataset files and migrates validated records into a structured SQL database.

---

## Technical Stack
* **Language:** Python 3.9+
* **Libraries:** Pandas, SQLAlchemy
* **Database:** SQLite / PostgreSQL
* **Version Control:** Git & GitHub

---

## Source-to-Target Data Mapping & Data Dictionary

| Source Field (`legacy_sales_data.csv`) | Target Field (`migrated_sales`) | Data Type | Transformation Applied |
| :--- | :--- | :--- | :--- |
| `Transaction_ID` | `Transaction_ID` | TEXT | Primary key deduplication (`drop_duplicates`) |
| `Customer_ID` | `Customer_ID` | TEXT | Direct mapping |
| `Transaction_Date` | `Transaction_Date` | DATE | Standardized mixed date formats (`MM/DD/YYYY`, `YYYY-MM-DD`) to `YYYY-MM-DD` |
| `Email` | `Email` | TEXT | Filled missing/null values with `'N/A'` |
| `Amount` | `Amount` | REAL/FLOAT | Direct mapping |

---

## Pipeline Architecture & Process

1. **Extract:** Reads 5,000 raw sales records from `legacy_sales_data.csv`.
2. **Transform:**
   * Removes duplicate rows based on unique `Transaction_ID`.
   * Fills missing customer email addresses with standard `'N/A'` placeholders.
   * Standardizes mixed date string formats to standard ISO `YYYY-MM-DD`.
3. **Load:** Connects via SQLAlchemy engine and loads cleansed data into the `migrated_sales` table.
4. **Validate:** Executes automated SQL queries to verify table record counts and confirm zero remaining duplicate entries.

---

## Execution & SQL Validation Results

### Pipeline Execution Output (`etl.py`)
```bash
Original row count: 5000
Cleaned row count: 501
ETL Pipeline executed successfully!
