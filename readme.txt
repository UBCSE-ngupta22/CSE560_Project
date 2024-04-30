# Inventory Management Database Project

## Dataset Description

The dataset used for this project is sourced from Kaggle and contains inventory management data. You can access the original dataset [here](https://www.kaggle.com/datasets/hetulparmar/inventory-management-dataset). The dataset consists of 28 columns and 401 rows, providing information about various aspects of inventory management.

## Tables and Data Import

To effectively utilize the dataset, it was organized into multiple tables within a relational database. The following tables were created to represent different entities and relationships within the inventory management system:

1. Location: Stores information about geographical locations.
2. Warehouse: Contains details about warehouses including their addresses and associated locations.
3. Employee: Holds employee information such as name, contact details, hire date, and job title.
4. Category: Represents product categories.
5. Product: Contains details about products including name, description, cost, price, and category.
6. Customer: Stores customer information including name, contact details, address, and credit limit.
7. OrderTable: Records order details including order date, status, and associated customer.
8. OrderItem: Contains information about individual items within orders including quantity, price, and associated product and order.

To populate these tables with data, dummy data was generated using SQL queries to simulate a real-world scenario. Each table was filled with relevant information to demonstrate the functionality of the inventory management system.

Below are the SQL queries used to populate the tables:

```sql
-- SQL queries for populating tables with dummy data
INSERT INTO Location (RegionName, CountryName, State, City, PostalCode)
SELECT
    'Region ' || (id % 10) + 1,
    'Country ' || (id % 50) + 1,
    'State ' || (id % 100) + 1,
    'City ' || (id % 500) + 1,
    'PostalCode ' || (id % 1000) + 1
FROM generate_series(1, 10000) as id;


INSERT INTO Warehouse (WarehouseAddress, WarehouseName, LocationID)
SELECT
    'WarehouseAddress ' || id,
    'WarehouseName ' || id,
    (id % 1000) + 1
FROM generate_series(1, 10000) as id;


INSERT INTO Employee (EmployeeEmail, EmployeeName, EmployeePhone, EmployeeHireDate, EmployeeJobTitle, WarehouseID)
SELECT
    'employee' || id || '@example.com',
    'EmployeeName ' || id,
    'EmployeePhone ' || id,
    CURRENT_DATE - INTERVAL '1 year' * (id % 5),
    'EmployeeJobTitle ' || id,
    (id % 1000) + 1
FROM generate_series(1, 10000) as id;

INSERT INTO Category (CategoryName)
VALUES
    ('Electronics'),
    ('Clothing'),
    ('Books'),
    ('Home Appliances');


INSERT INTO Product (ProductName, ProductDescription, ProductStandardCost, Profit, ProductListPrice, CategoryID)
SELECT
    'Product ' || id,
    'ProductDescription ' || id,
    (id % 1000) + 10,
    (id % 10) + 1,
    (id % 1000) + 50,
    (id % 4) + 1
FROM generate_series(1, 10000) as id;


INSERT INTO Customer (CustomerEmail, CustomerName, CustomerAddress, CustomerCreditLimit, CustomerPhone)
SELECT
    'customer' || id || '@example.com',
    'CustomerName ' || id,
    'CustomerAddress ' || id,
    (id % 10000) + 100,
    'CustomerPhone ' || id
FROM generate_series(1, 10000) as id;


INSERT INTO OrderTable (OrderDate, Status, CustomerID)
SELECT
    CURRENT_DATE - INTERVAL '1 month' * (id % 12),
    CASE WHEN random() < 0.5 THEN 'Pending' ELSE 'Completed' END,
    (id % 10000) + 1
FROM generate_series(1, 10000) as id;


INSERT INTO OrderItem (OrderID, ProductID, OrderItemQuantity, PerUnitPrice, TotalItemQuantity)
SELECT
    (id % 10000) + 1,
    (id % 10000) + 1,
    (id % 10) + 1,
    (id % 100) + 10,
    (id % 10) + 1
FROM generate_series(1, 10000) as id;
```

## Instructions

1. Ensure you have PostgreSQL installed on your system.
2. Create a new database and execute the provided SQL queries to create tables and populate them with data.
3. Once the database is set up, you can perform various queries and analyses to explore the inventory management data.

## References

- Kaggle Dataset: [Inventory Management Dataset](https://www.kaggle.com/datasets/hetulparmar/inventory-management-dataset)