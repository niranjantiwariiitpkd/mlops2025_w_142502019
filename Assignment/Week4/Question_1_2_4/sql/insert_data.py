import pandas as pd
from sqlalchemy import create_engine

print("Script started")

try:
    # Connect to PostgreSQL
    engine = create_engine("postgresql://postgres@localhost:5432/online_retail")
    with engine.connect() as conn:
        print("Connected to PostgreSQL successfully!")

    # Load dataset
    df = pd.read_excel("data/Online Retail.xlsx")
    print("Excel file loaded")

    # Clean and prepare
    df.dropna(subset=["CustomerID"], inplace=True)
    df = df.head(1000)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["CustomerID"] = df["CustomerID"].astype(str)
    df["StockCode"] = df["StockCode"].astype(str)

    print("Data cleaned")

    # Insert into Customer table
    df[["CustomerID", "Country"]].drop_duplicates().to_sql("Customer", engine, if_exists="append", index=False)
    print("Customer table inserted")

    # Insert into Product table
    df[["StockCode", "Description", "UnitPrice"]].drop_duplicates().to_sql("Product", engine, if_exists="append", index=False)
    print("Product table inserted")

    # Insert into Invoice table
    df[["InvoiceNo", "InvoiceDate", "CustomerID"]].drop_duplicates().to_sql("Invoice", engine, if_exists="append", index=False)
    print("Invoice table inserted")

    # Insert into InvoiceDetails table
    df[["InvoiceNo", "StockCode", "Quantity"]].to_sql("InvoiceDetails", engine, if_exists="append", index=False)
    print("InvoiceDetails table inserted")

    print(" All data inserted successfully!")

except Exception as e:
    print("Error occurred:", e)