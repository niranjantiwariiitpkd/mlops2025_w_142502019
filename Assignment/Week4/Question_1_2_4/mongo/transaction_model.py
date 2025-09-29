import pandas as pd
from pymongo import MongoClient

# Connect to Atlas
client = MongoClient("mongodb+srv://142502019:Kabaddi@cluster0.epqcybp.mongodb.net/?retryWrites=true&w=majority")
db = client["OnlineRetail"]
collection = db["TransactionCentric"]

# Load and clean data
df = pd.read_excel("data/Online Retail.xlsx")
df.dropna(subset=["CustomerID"], inplace=True)
df = df.head(1000)

# Group by invoice
grouped = df.groupby("InvoiceNo")

docs = []
for invoice_no, group in grouped:
    doc = {
        "InvoiceNo": invoice_no,
        "InvoiceDate": group["InvoiceDate"].iloc[0],
        "CustomerID": str(group["CustomerID"].iloc[0]),
        "Country": group["Country"].iloc[0],
        "Items": group[["StockCode", "Description", "Quantity", "UnitPrice"]].to_dict("records")
    }
    docs.append(doc)

collection.insert_many(docs)
print(" Transaction-centric documents inserted")