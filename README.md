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

## 🛠️ Using the Scripts

This project includes Python scripts to generate OLAP cube data from the Northwind database and prepare it for MongoDB import.

### 📋 Prerequisites

- Python 3.9 or higher
- Required Python packages (install using):
  ```
  pip install -r requirements.txt
  ```
- MongoDB (for importing the generated data)

### 🔄 Generating OLAP Cubes

The scripts automatically download the Northwind database and transform it into MongoDB-compatible CSV files:

1. **Run all cubes at once:**
   ```
   python scripts/generate_all_cubes.py
   ```
   This will generate all cubes and validate them automatically.

2. **Run individual cube generators:**
   ```
   python scripts/generate_cube1.py  # Customer and employee data
   python scripts/generate_cube2.py  # Supplier and product data
   python scripts/generate_cube3.py  # Customer order and sales levels
   python scripts/generate_cube4.py  # Revenue analysis data
   ```

### 🔍 Validating OLAP Cubes

You can validate the generated cube CSV files to ensure they're properly structured:

```bash
python scripts/validate_cubes.py
```

The validation script checks:
- File existence
- Presence of all required columns
- Data integrity (no missing critical values)
- Overall data quality

Each cube is validated against its expected schema, and a summary report is provided.

## 🐳 Using MongoDB with Docker

### Setting Up MongoDB Container

If you don't have MongoDB installed locally, you can easily run it in a Docker container:

1. **Make sure Docker is installed** on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop/).

2. **Run a MongoDB container** with the following command:
   ```bash
   docker run --name mongodb -d -p 27017:27017 mongo:latest
   ```
   This command:
   - Creates a container named "mongodb"
   - Runs it in detached mode (-d)
   - Maps the MongoDB port from the container to your local machine (-p 27017:27017)
   - Uses the latest MongoDB image

3. **Verify the container is running**:
   ```bash
   docker ps
   ```

### Executing MongoDB Commands

You can interact with the MongoDB container in several ways:

1. **Using Docker exec to run commands**:
   ```bash
   docker exec -it mongodb mongosh
   ```
   This opens the MongoDB shell where you can execute commands directly.

2. **Import the OLAP cube data into the container**:
   ```bash
   # First, copy all CSV files into the container
   docker cp output/cube1.csv mongodb:/tmp/cube1.csv
   docker cp output/cube2.csv mongodb:/tmp/cube2.csv
   docker cp output/cube3.csv mongodb:/tmp/cube3.csv
   docker cp output/cube4.csv mongodb:/tmp/cube4.csv
   
   # Then import each cube into MongoDB
   docker exec -it mongodb mongoimport --db northwind_olap --collection cube1 --type csv --headerline --file /tmp/cube1.csv
   docker exec -it mongodb mongoimport --db northwind_olap --collection cube2 --type csv --headerline --file /tmp/cube2.csv
   docker exec -it mongodb mongoimport --db northwind_olap --collection cube3 --type csv --headerline --file /tmp/cube3.csv
   docker exec -it mongodb mongoimport --db northwind_olap --collection cube4 --type csv --headerline --file /tmp/cube4.csv
   ```

### 🔍 Exploring Data with MongoDB Compass

MongoDB Compass is a powerful GUI tool for exploring and manipulating MongoDB data visually.

1. **Download and install MongoDB Compass** from the [official MongoDB website](https://www.mongodb.com/products/compass).

2. **Connect to your MongoDB instance**:
   - Open MongoDB Compass
   - Connect using the connection string: `mongodb://localhost:27017`
   - You should see the `northwind_olap` database in the list

3. **Explore your OLAP cubes**:
   - Click on the `northwind_olap` database
   - Browse collections (cube1, cube2, etc.)
   - Use the query builder to construct OLAP queries
   - Visualize data using Compass's built-in charts and aggregation pipeline builder

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.