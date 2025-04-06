# 🚀 OLAP in NoSQL with MongoDB

## 📋 Overview
Implementation of an OLAP (Online Analytical Processing) solution in a NoSQL environment using MongoDB.

## 🧩 OLAP Concepts

### 📊 What is OLAP?
OLAP (Online Analytical Processing) is a technology that enables multidimensional analysis of business data, allowing users to view data from different perspectives for decision-making.

### 📦 OLAP Cube Properties
- **Multidimensional** - Data viewed across multiple dimensions
- **Integrated** - Unified data from multiple sources
- **Time-variant** - Historical data tracked over time
- **Non-volatile** - Data stable once loaded

### 🔢 Dimensions & Dimension Tables
Dimensions represent business perspectives (time, product, location). Dimension tables store descriptive attributes related to these business entities.

### 📐 Dimensional Models
- **Star Schema** - Central fact table connected to dimension tables
- **Snowflake Schema** - Normalized dimension tables
- **Galaxy Schema** - Multiple fact tables sharing dimension tables

### 📏 Analysis Measures
Numeric values (facts) analyzed across dimensions (sales amount, quantity, counts). These are typically stored in fact tables.

### 🌲 Dimension Hierarchy
Logical structure organizing dimension members into levels (Year > Quarter > Month > Day), enabling drill-down and roll-up operations.

## 🧮 OLAP Algebra Operations

### 🔍 Core OLAP Operations
- **Roll-up** (↗️) - Aggregating data by climbing up hierarchy or dimension reduction
- **Drill-down** (↘️) - Breaking down aggregated data into more detailed levels
- **Slice** (🔪) - Selecting a specific dimension value to create a subset of the cube
- **Dice** (🎲) - Creating a subcube by filtering on multiple dimensions
- **Pivot** (🔄) - Rotating the cube to view data from different perspectives

### 🔧 Extended Operations
- **Drill-through** - Accessing detailed data behind aggregated cells
- **Drill-across** - Analyzing related data across multiple fact tables
- **Consolidation** - Computing aggregate values using various functions (SUM, AVG, MIN, MAX)

## 💡 Why NoSQL?
NoSQL became popular among Internet giants (Google, Facebook, Amazon) handling massive data volumes. When traditional RDBMS slow down under huge data loads, two scaling options emerge:
- **Scale Up** (↕️) - Upgrading existing hardware (costly)
- **Scale Out** (↔️) - Distributing database load across multiple hosts as demand increases

NoSQL databases excel at horizontal scaling (scale-out), making them ideal for big data applications and analytics workloads like OLAP.

## 🍃 Why MongoDB?
MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like documents. Key advantages for OLAP implementation:

- **Document Model** 📄 - Intuitive representation of multidimensional data structures
- **Dynamic Schema** 🔄 - Adapts to changing reporting requirements without downtime
- **Aggregation Framework** 📊 - Powerful pipeline for OLAP operations (grouping, filtering, projecting)
- **Horizontal Scalability** 📈 - Sharding for distributing data across multiple servers
- **Indexing Capabilities** 🔍 - Support for complex queries and aggregations at scale
- **Map-Reduce** 🗺️ - Advanced computational operations for complex analytics
- **High Performance** ⚡ - In-memory processing options for faster analytics

MongoDB bridges relational and non-relational worlds, making it ideal for implementing OLAP solutions while maintaining NoSQL's scalability benefits.

## 💫 Star Schema Migration to MongoDB

### 🔄 Transformation Process
- **Fact Table** → MongoDB Collection with embedded metrics/measures
- **Dimension Tables** → Can be implemented in several ways:
  - 📑 Embedded subdocuments (denormalization)
  - 🔗 Document references (normalization)
  - 🔀 Hybrid approach based on access patterns

### 📝 Example Migration
#### Star Schema Example
- **Fact Table**: `TF_Revenue` (OrderMonth, CustomerID, ProductID, OrdersRevenue, ShippedRevenue)
- **Dimension Tables**:
  - `TD_Time` (OrderMonth, OrderYear)
  - `TD_Customers` (CustomerID, CustomerName, City, Country)
  - `TD_Products` (ProductID, ProductName, CategoryID, CategoryName)

#### MongoDB Document Model
```javascript
{
  "_id": 22333,
  "OrdersRevenue": 5,
  "ShippedRevenue": 6,
  "OrderMonth": "3-2021",
  "OrderYear": "2021",
  "Customer": {
    "CustomerID": 105,
    "CustomerName": "Mohamed",
    "City": "Hadjout",
    "Country": "Algeria"
  },
  "Product": {
    "ProductID": 522,
    "ProductName": "Nike",
    "CategoryID": 55,
    "CategoryName": "Shoes"
  }
}
```

## 📄 OLAP Cubes Overview

For a detailed description of the four OLAP cubes used in this project, refer to the [OLAP Cubes Overview](cubes-overview.md) document.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.