import streamlit as st
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Inventory Management System", page_icon=":bar_chart:")

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Add title
st.title("Inventory Management System")

# Query 1: Product Sales Over Time
query_1 = "SELECT OrderDate, SUM(PerUnitPrice * OrderItemQuantity) AS TotalSales FROM OrderItem JOIN OrderTable ON OrderItem.OrderID = OrderTable.OrderID GROUP BY OrderDate;"
df_1 = conn.query(query_1, ttl="10m")
st.subheader("Product Sales Over Time")
st.line_chart(df_1.set_index('orderdate'))

# Query 2: Top Selling Products
query_2 = """
SELECT p.ProductName, SUM(oi.OrderItemQuantity) AS TotalQuantitySold
FROM OrderItem oi
INNER JOIN Product p ON oi.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalQuantitySold DESC
LIMIT 5;
"""
df_2 = conn.query(query_2, ttl="10m")
st.subheader("Top Selling Products")
st.bar_chart(df_2.set_index('productname'))

# Query 3: Employees by Warehouse
query_3 = """
SELECT e.EmployeeName, w.WarehouseName
FROM Employee e
INNER JOIN Warehouse w ON e.WarehouseID = w.WarehouseID
LIMIT 50;
"""
df_3 = conn.query(query_3, ttl="10m")
st.subheader("Employees by Warehouse")
st.write(df_3)

# Query 4: Profit Margin Analysis
query_4 = "SELECT ProductName, Profit / ProductListPrice AS ProfitMargin FROM Product;"
df_4 = conn.query(query_4, ttl="10m")
st.subheader("Profit Margin Analysis")
st.bar_chart(df_4.set_index('productname'))

# Query 5: Customer Spending Habits
query_5 = "SELECT CustomerName, SUM(PerUnitPrice * OrderItemQuantity) AS TotalSpending FROM OrderItem JOIN OrderTable ON OrderItem.OrderID = OrderTable.OrderID JOIN Customer ON OrderTable.CustomerID = Customer.CustomerID GROUP BY CustomerName;"
df_5 = conn.query(query_5, ttl="10m")
st.subheader("Customer Spending Habits")
st.bar_chart(df_5.set_index('customername'))

# Query 6: Total Sales by Category
query_6 = """
SELECT c.CategoryName, SUM(oi.PerUnitPrice * oi.OrderItemQuantity) AS TotalSales
FROM OrderItem oi
INNER JOIN Product p ON oi.ProductID = p.ProductID
INNER JOIN Category c ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName;
"""
df_6 = conn.query(query_6, ttl="10m")
st.subheader("Total Sales by Category")
st.bar_chart(df_6.set_index('categoryname'))

# Query 7: Top 10 Customers with Highest Credit Limit Distribution
query_7 = """
SELECT CustomerName, CustomerCreditLimit
FROM Customer
ORDER BY CustomerCreditLimit DESC
LIMIT 10;
"""
df_7 = conn.query(query_7, ttl="10m")
st.subheader("Top 10 Customers with Highest Credit Limit Distribution")
st.bar_chart(df_7.set_index('customername'))

# Query 8: Product Category Distribution
query_8 = "SELECT CategoryName, COUNT(*) AS Count FROM Product JOIN Category ON Product.CategoryID = Category.CategoryID GROUP BY CategoryName;"
df_8 = conn.query(query_8, ttl="10m")
st.subheader("Product Category Distribution")
st.bar_chart(df_8.set_index('categoryname'))

# Query 9: Warehouse Distribution by Region
query_9 = """
SELECT l.RegionName, COUNT(w.WarehouseID) AS WarehouseCount
FROM Warehouse w
INNER JOIN Location l ON w.LocationID = l.LocationID
GROUP BY l.RegionName;
"""
df_9 = conn.query(query_9, ttl="10m")
st.subheader("Warehouse Distribution by Region")
st.plotly_chart(px.pie(df_9, values='warehousecount', names='regionname'))

# Query 10: Average Order Value Over Time
query_10 = "SELECT OrderDate, AVG(PerUnitPrice * OrderItemQuantity) AS AverageOrderValue FROM OrderItem JOIN OrderTable ON OrderItem.OrderID = OrderTable.OrderID GROUP BY OrderDate;"
df_10 = conn.query(query_10, ttl="10m")
st.subheader("Average Order Value Over Time")
st.line_chart(df_10.set_index('orderdate'))

