# MongoDB Implementation

## Why NoSQL?

NoSQL became popular among Internet giants (Google, Facebook, Amazon) handling massive data volumes. When traditional RDBMS slow down under huge data loads, two scaling options emerge:

- **Scale Up** - Upgrading existing hardware (costly)
- **Scale Out** - Distributing database load across multiple hosts as demand increases

NoSQL databases excel at horizontal scaling (scale-out), making them ideal for big data applications and analytics workloads like OLAP.

## Why MongoDB?

MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like documents. Key advantages for OLAP implementation:

- **Document Model** - Intuitive representation of multidimensional data structures
- **Dynamic Schema** - Adapts to changing reporting requirements without downtime
- **Aggregation Framework** - Powerful pipeline for OLAP operations (grouping, filtering, projecting)
- **Horizontal Scalability** - Sharding for distributing data across multiple servers
- **Indexing Capabilities** - Support for complex queries and aggregations at scale
- **Map-Reduce** - Advanced computational operations for complex analytics
- **High Performance** - In-memory processing options for faster analytics

## 💫 Star Schema Migration to MongoDB

### Transformation Process

- **Fact Table** → MongoDB Collection with embedded metrics/measures
- **Dimension Tables** → Can be implemented in several ways:
  - Embedded subdocuments (denormalization)
  - Document references (normalization)
  - Hybrid approach based on access patterns

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
