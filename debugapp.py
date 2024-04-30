import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

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

# # Query 3: Inventory Levels by Warehouse
# query_3 = "SELECT p.ProductName, w.WarehouseName, SUM(oi.TotalItemQuantity) AS TotalInventory FROM OrderItem oi JOIN Product p ON oi.ProductID = p.ProductID JOIN Warehouse w ON p.CategoryID = w.CategoryID GROUP BY p.ProductName, w.WarehouseName;"
# df_3 = conn.query(query_3, ttl="10m")
# st.subheader("Inventory Levels by Warehouse")
# st.dataframe(df_3)

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

# # Query 6: Order Status Distribution
# query_6 = "SELECT Status, COUNT(*) AS Count FROM OrderTable GROUP BY Status;"
# df_6 = conn.query(query_6, ttl="10m")
# st.subheader("Order Status Distribution")
# st.bar_chart(df_6.set_index('Status'))

# # Query 7: Employee Performance
# query_7 = "SELECT EmployeeName, COUNT(*) AS TotalOrders FROM Employee JOIN OrderTable ON Employee.WarehouseID = OrderTable.WarehouseID GROUP BY EmployeeName;"
# df_7 = conn.query(query_7, ttl="10m")
# st.subheader("Employee Performance")
# st.bar_chart(df_7.set_index('employeename'))

# Query 8: Product Category Distribution
query_8 = "SELECT CategoryName, COUNT(*) AS Count FROM Product JOIN Category ON Product.CategoryID = Category.CategoryID GROUP BY CategoryName;"
df_8 = conn.query(query_8, ttl="10m")
st.subheader("Product Category Distribution")
st.bar_chart(df_8.set_index('categoryname'))

# # Query 9: Geographical Sales Distribution
# query_9 = "SELECT RegionName, SUM(PerUnitPrice * OrderItemQuantity) AS TotalSales FROM OrderItem JOIN OrderTable ON OrderItem.OrderID = OrderTable.OrderID JOIN Warehouse ON OrderTable.WarehouseID = Warehouse.WarehouseID JOIN Location ON Warehouse.LocationID = Location.LocationID GROUP BY RegionName;"
# df_9 = conn.query(query_9, ttl="10m")
# st.subheader("Geographical Sales Distribution")
# st.bar_chart(df_9.set_index('regionname'))

# Query 10: Average Order Value Over Time
query_10 = "SELECT OrderDate, AVG(PerUnitPrice * OrderItemQuantity) AS AverageOrderValue FROM OrderItem JOIN OrderTable ON OrderItem.OrderID = OrderTable.OrderID GROUP BY OrderDate;"
df_10 = conn.query(query_10, ttl="10m")
st.subheader("Average Order Value Over Time")
st.line_chart(df_10.set_index('orderdate'))




