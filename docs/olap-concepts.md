# 🧩 OLAP Concepts

## 📊 What is OLAP?

OLAP (Online Analytical Processing) is a technology that enables multidimensional analysis of business data, allowing users to view data from different perspectives for decision-making.

## 📦 OLAP Cube Properties

- **Multidimensional** - Data viewed across multiple dimensions
- **Integrated** - Unified data from multiple sources
- **Time-variant** - Historical data tracked over time
- **Non-volatile** - Data stable once loaded

## 🔢 Dimensions & Dimension Tables

Dimensions represent business perspectives (time, product, location). Dimension tables store descriptive attributes related to these business entities.

## 📐 Dimensional Models

- **Star Schema** - Central fact table connected to dimension tables
- **Snowflake Schema** - Normalized dimension tables
- **Galaxy Schema** - Multiple fact tables sharing dimension tables

## 📏 Analysis Measures

Numeric values (facts) analyzed across dimensions (sales amount, quantity, counts). These are typically stored in fact tables.

## 🌲 Dimension Hierarchy

Logical structure organizing dimension members into levels (Year > Quarter > Month > Day), enabling drill-down and roll-up operations.
