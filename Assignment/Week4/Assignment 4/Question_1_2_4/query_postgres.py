import psycopg2
import time

try:
    conn = psycopg2.connect(
        database="uci_online_retail",
        user="postgres",
        password="your_password", 
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    print("Connected to PostgreSQL")

    # INSERT
    start = time.time()
    cur.execute("INSERT INTO Customers (CustomerID, Country) VALUES (99999, 'India')")
    conn.commit()
    print("INSERT time:", time.time() - start)

    # SELECT
    start = time.time()
    cur.execute("SELECT * FROM Customers WHERE Country = 'India'")
    rows = cur.fetchall()
    print("SELECT time:", time.time() - start)
    print("Rows:", rows)

    # UPDATE
    start = time.time()
    cur.execute("UPDATE Customers SET Country = 'Bharat' WHERE CustomerID = 99999")
    conn.commit()
    print("UPDATE time:", time.time() - start)

    # DELETE
    start = time.time()
    cur.execute("DELETE FROM Customers WHERE CustomerID = 99999")
    conn.commit()
    print("DELETE time:", time.time() - start)

    cur.close()
    conn.close()

except psycopg2.OperationalError as e:
    print("Connection failed:", e)