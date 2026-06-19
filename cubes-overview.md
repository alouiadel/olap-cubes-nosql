# OLAP Cubes Overview

This document provides an overview of the four OLAP cubes used in this project. Each cube represents a specific aspect of the data modeled for analytical purposes.

## Cube 1

- **Description**: Contains customer and employee-related data, along with order details.
- **Attributes**:
  - `customerID`: Customer identifier.
  - `customerName`: Customer name.
  - `customerCity`: Customer city.
  - `customerCountry`: Customer country.
  - `employeeID`: Employee identifier.
  - `employeeName`: Employee full name.
  - `employeeCity`: Employee city.
  - `employeeCountry`: Employee country.
  - `orderMonth`: Month identifier.
  - `orderYear`: Year.
  - `shipOrders`: Number of shipped orders.
  - `notShipOrders`: Number of unshipped orders.

## Cube 2

- **Description**: Focuses on supplier and product category data.
- **Attributes**:
  - `supplierID`: Supplier identifier.
  - `supplierName`: Supplier name.
  - `supplierCity`: Supplier city.
  - `supplierCountry`: Supplier country.
  - `categorieID`: Product category identifier.
  - `categorieName`: Category name.
  - `priceLevel`: Price level.
  - `stockLevel`: Stock level.
  - `produit_num`: Number of products.

## Cube 3

- **Description**: Provides insights into customer orders and sales levels.
- **Attributes**:
  - `customerCity`: Customer city.
  - `customerCountry`: Customer country.
  - `orderLevel`: Importance of customer orders.
  - `salesLevel`: Sales level achieved with the customer.
  - `customer_num`: Number of customers.

## Cube 4

- **Description**: Combines product, order, and customer data for revenue analysis.
- **Attributes**:
  - `ProductID`: Product identifier.
  - `ProductName`: Product name.
  - `CategoryID`: Category identifier.
  - `ordersRevenue`: Revenue from orders.
  - `ShippedRevenue`: Revenue from shipped orders.
  - `customerID`: Customer identifier.
  - `customerName`: Customer name.
  - `customerCity`: Customer city.
  - `customerCountry`: Customer country.
  - `orderMonth`: Order month identifier.
  - `orderYear`: Order year.
