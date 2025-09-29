
import pandas as pd
from mongo_models import get_client, setup_db, insert_transaction_doc, insert_customer_doc

EXCEL_FILE = "Online_Retail.xlsx"

df = pd.read_excel(EXCEL_FILE)

df = df.dropna(subset=["CustomerID"])
df["CustomerID"] = df["CustomerID"].astype(int)

client = get_client()
db = setup_db(client)

for invoice_no, group in df.groupby("InvoiceNo"):
    
    invoice_doc = {
        "InvoiceNo": invoice_no,
        "InvoiceDate": group["InvoiceDate"].iloc[0],
        "CustomerID": int(group["CustomerID"].iloc[0]),
        "Country": group["Country"].iloc[0],
        "items": [
            {
                "StockCode": str(row["StockCode"]),
                "Description": row["Description"],
                "Quantity": int(row["Quantity"]),
                "UnitPrice": float(row["UnitPrice"])
            }
            for _, row in group.iterrows()
        ]
    }
    insert_transaction_doc(db, invoice_doc)

    customer_doc = {
        "CustomerID": int(group["CustomerID"].iloc[0]),
        "Country": group["Country"].iloc[0],
        "invoices": [
            {
                "InvoiceNo": invoice_no,
                "InvoiceDate": group["InvoiceDate"].iloc[0],
                "items": [
                    {
                        "StockCode": str(row["StockCode"]),
                        "Description": row["Description"],
                        "Quantity": int(row["Quantity"]),
                        "UnitPrice": float(row["UnitPrice"])
                    }
                    for _, row in group.iterrows()
                ]
            }
        ]
    }
    insert_customer_doc(db, customer_doc)

print("Data loaded into MongoDB successfully!")
