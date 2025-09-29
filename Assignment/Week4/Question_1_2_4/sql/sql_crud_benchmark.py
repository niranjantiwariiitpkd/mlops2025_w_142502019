from sqlalchemy import create_engine, text
from datetime import datetime

print("SQL CRUD Benchmark Started")

# Connect to PostgreSQL
engine = create_engine("postgresql://postgres@localhost:5432/online_retail")

with engine.connect() as conn:
    print("Connected to PostgreSQL")

    #  Read
    start = datetime.now()
    result = conn.execute(text('SELECT * FROM "Invoice" WHERE "InvoiceNo" = \'536365\''))
    rows = result.fetchall()
    print("PostgreSQL Read Time:", datetime.now() - start)

    #  Update
    start = datetime.now()
    conn.execute(text('UPDATE "InvoiceDetails" SET "Quantity" = 10 WHERE "InvoiceNo" = \'536365\' AND "StockCode" = \'85123A\''))
    print("PostgreSQL Update Time:", datetime.now() - start)

    #  Insert
    start = datetime.now()
    conn.execute(text('INSERT INTO "Invoice" ("InvoiceNo", "InvoiceDate", "CustomerID") VALUES (\'TEST999\', NOW(), \'99999\')'))
    conn.execute(text('INSERT INTO "InvoiceDetails" ("InvoiceNo", "StockCode", "Quantity") VALUES (\'TEST999\', \'NEW1\', 1)'))
    print("PostgreSQL Insert Time:", datetime.now() - start)

    #  Delete
    start = datetime.now()
    conn.execute(text('DELETE FROM "InvoiceDetails" WHERE "InvoiceNo" = \'TEST999\''))
    conn.execute(text('DELETE FROM "Invoice" WHERE "InvoiceNo" = \'TEST999\''))
    print("PostgreSQL Delete Time:", datetime.now() - start)