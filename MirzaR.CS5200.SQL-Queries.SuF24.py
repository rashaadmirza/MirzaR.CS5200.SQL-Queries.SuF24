# ASSIGNMENT 06.2: Query a Database with SQL in Python
# Date: June 18, 2024
# Name: Rashaad Mohammed Mirza

# Importing the sqlite3 module to work with SQLite databases
import sqlite3

# ------------------------------------------------
# 1. Connect to the SQLite database from Python.
# ------------------------------------------------
conn = sqlite3.connect('OrdersDB.sqlitedb.db')
cursor = conn.cursor()

# ------------------------------------------------
# 2. What are the last name, first name, and birth date of all employees, sorted by last name? Print the result set.
# ------------------------------------------------
query = """
SELECT LastName, FirstName, BirthDate
FROM Employees
ORDER BY LastName;
"""

# Execute the query
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()

# Print the result set
for row in results:
    print(f"Last Name: {row[0]}, First Name: {row[1]}, Birth Date: {row[2]}")

# ------------------------------------------------
# 3. What is the total number of orders placed by each customer. Display the result.
# ------------------------------------------------
query_orders = """
SELECT Customers.CustomerName, COUNT(Orders.OrderID) AS TotalOrders
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerID
ORDER BY Customers.CustomerID;
"""

# Execute the query for orders
cursor.execute(query_orders)

# Fetch all results for orders
order_results = cursor.fetchall()

# Print the result set for orders
print("\nTotal number of orders placed by each customer:")
for row in order_results:
    print(f"Customer Name: {row[0]}, Total Orders: {row[1]}")
    
# ------------------------------------------------
# 4. Display all of the categories.
# ------------------------------------------------
query_categories = """
SELECT CategoryID, CategoryName, Description
FROM Categories;
"""

# Execute the query for categories
cursor.execute(query_categories)

# Fetch all results for categories
category_results = cursor.fetchall()

# Print the result set for categories
print("\nAll Categories:")
for row in category_results:
    print(f"Category ID: {row[0]}, Category Name: {row[1]}, Description: {row[2]}")

# ------------------------------------------------
# 5. Close the connection to the database.
# ------------------------------------------------
conn.close()
