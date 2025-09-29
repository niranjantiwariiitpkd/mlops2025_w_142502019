#  Online Retail Relational Pipeline (PostgreSQL)

project loads and normalizes the Online Retail dataset into a PostgreSQL database using Python and pandas.
It prepares four relational tables—`customers`, `products`, `invoices`, and `invoiceitems`—with basic cleaning,
deduplication, and validation.

---

##  Setup Instructions

1. **Install dependencies**
   ```bash
   pip install pandas sqlalchemy psycopg2 openpyxl
   ```

2. **Start PostgreSQL and create the database**
   ```sql
   CREATE DATABASE uci_online_retail;
   ```

3. **Update connection URI in `load_relational.py`**
   ```python
   DB_URI = "postgresql+psycopg2://postgres@localhost:5432/uci_online_retail"
   ```

4. **Place `Online_Retail.xlsx` in the same directory as the script**

---

## Execution

Run the script to load and insert data:
```bash
  python load_relational.py
```
This performs:
- Data cleaning and type conversion
- Deduplication by primary keys
- Column normalization to lowercase
- Bulk inserts using SQLAlchemy



## Table Overview

| Table         | Primary Key     | Description                          |
|---------------|------------------|--------------------------------------|
| `customers`   | `customerid`     | Unique customers and their country   |
| `products`    | `stockcode`      | Unique products and unit prices      |
| `invoices`    | `invoiceno`      | Invoice metadata and customer links  |
| `invoiceitems`| *(none)*         | Line items per invoice and product   |

---

## Validation

After insertion, the script prints:

 Inserted records successfully.
 InvoiceItems count: 5000


You can manually verify with:
```sql
SELECT COUNT(*) FROM invoiceitems;
SELECT DISTINCT country FROM customers;
```

---

## Deduplication Logic

- `products`: deduplicated by `stockcode`
- `customers`: deduplicated by `customerid`
- `invoices`: deduplicated by `invoiceno`
- `invoiceitems`: no primary key; all rows inserted

---

##  MongoDB Comparison (for Part 3)

When comparing with MongoDB:
- PostgreSQL enforces schema and constraints (e.g., primary keys)
- MongoDB allows nested documents and flexible schemas
- Insert conflicts (e.g., duplicate keys) are handled differently
- Querying and indexing strategies vary by model

---
