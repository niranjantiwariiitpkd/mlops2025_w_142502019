# Online Retail Assignment – SQL (2NF)

## Setup
- PostgreSQL database: `online_retail`
- Tables: `Customer`, `Product`, `Invoice`, `InvoiceDetails`
- Inserted 1000 records from UCI Online Retail dataset

## How to Run
```bash
pip install -r sql/requirements.txt
python sql/insert_data.py

## SQL Schema

The 2NF schema is defined in `sql/schema.sql`. It can be executed manually in pgAdmin or any PostgreSQL client to recreate the database structure.

## Question 3: CRUD + Performance

CRUD operations implemented for both models:
- Transaction-centric: fast invoice lookup, simple updates
- Customer-centric: nested updates, better customer history

Performance measured using `datetime.now()` for read latency.
## Question 3: CRUD Operations & Performance

### Customer-Centric Model
- Read by CustomerID: 
- Update nested invoice: 
- Insert new invoice: 
- Delete customer: 
- Read latency: ~0.75s

### Transaction-Centric Model
- Read by InvoiceNo: 
- Update item quantity: 
- Insert/delete invoice: 
- Read latency: ~0.62s

### Summary
- Transaction model is faster for invoice lookup
- Customer model is better for historical aggregation

## Question 4: SQL vs MongoDB Comparison

SQL excels in structured, relational data with integrity constraints. MongoDB offers agility and performance for nested, document-centric models. For Online Retail:
- SQL is ideal for normalized reporting and analytics
- MongoDB is better for fast invoice lookup and customer history

Both models were implemented, benchmarked, and validated using real data.