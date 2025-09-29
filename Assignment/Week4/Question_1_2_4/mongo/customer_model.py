import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb+srv://142502019:Kabaddi@cluster0.epqcybp.mongodb.net/?retryWrites=true&w=majority")
db = client["OnlineRetail"]
collection = db["CustomerCentric"]

df = pd.read_excel("data/Online Retail.xlsx")
df.dropna(subset=["CustomerID"], inplace=True)
df = df.head(1000)

grouped = df.groupby("CustomerID")

docs = []
for cust_id, group in grouped:
    invoices = []
    for invoice_no, inv_group in group.groupby("InvoiceNo"):
        invoices.append({
            "InvoiceNo": invoice_no,
            "InvoiceDate": inv_group["InvoiceDate"].iloc[0],
            "Items": inv_group[["StockCode", "Description", "Quantity", "UnitPrice"]].to_dict("records")
        })
    doc = {
        "CustomerID": str(cust_id),
        "Country": group["Country"].iloc[0],
        "Invoices": invoices
    }
    docs.append(doc)

collection.insert_many(docs)
print(" Customer-centric documents inserted")