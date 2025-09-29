-- Customer Table
CREATE TABLE Customer (
    CustomerID VARCHAR(10) PRIMARY KEY,
    Country VARCHAR(50)
);

-- Product Table
CREATE TABLE Product (
    StockCode VARCHAR(10) PRIMARY KEY,
    Description TEXT,
    UnitPrice FLOAT
);

-- Invoice Table
CREATE TABLE Invoice (
    InvoiceNo VARCHAR(10) PRIMARY KEY,
    InvoiceDate TIMESTAMP,
    CustomerID VARCHAR(10),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- InvoiceDetails Table
CREATE TABLE InvoiceDetails (
    InvoiceNo VARCHAR(10),
    StockCode VARCHAR(10),
    Quantity INT,
    PRIMARY KEY (InvoiceNo, StockCode),
    FOREIGN KEY (InvoiceNo) REFERENCES Invoice(InvoiceNo),
    FOREIGN KEY (StockCode) REFERENCES Product(StockCode)
);


-- This schema satisfies 2NF:
-- - No partial dependencies.
-- - Each table has atomic attributes.
-- - Foreign keys maintain integrity.
