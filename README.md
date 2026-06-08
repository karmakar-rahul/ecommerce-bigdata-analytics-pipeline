# E-Commerce Big Data Analytics Pipeline

## Overview

An end-to-end Big Data Analytics platform built using Hadoop, Spark, Hive, and Streamlit for processing and visualizing large-scale e-commerce transaction data.

The project simulates a real-world e-commerce environment by generating synthetic customer, product, order, and payment data, processing it through a distributed data pipeline, and presenting business insights through an interactive dashboard.

---

## Architecture

```text
Synthetic Data Generation
          ↓
     Hadoop HDFS
          ↓
     Spark ETL
          ↓
     Hive Warehouse
          ↓
    Analytics Layer
          ↓
 Streamlit Dashboard
```

---

## Technology Stack

* Python
* Hadoop HDFS
* Apache Spark (PySpark)
* Hive
* MySQL Metastore
* Streamlit
* Plotly
* Pandas

---

## Features

* Generated 1M+ synthetic e-commerce transactions
* Distributed data storage using Hadoop HDFS
* Spark-based ETL pipelines for large-scale data processing
* Hive data warehouse for analytical querying
* KPI generation for business intelligence reporting
* Interactive Streamlit dashboard for data visualization

---

## Analytics Implemented

* Revenue by Category
* Revenue by State
* Product Performance Analysis
* Payment Success vs Refund Analysis
* Customer Segment Modeling
* Seasonal Revenue Trends

---

## Project Structure

```text
ecommerce-bigdata-analytics-pipeline
│
├── analytics/
├── dashboard/
├── generators/
├── spark/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Enhancements

* Kafka-based Real-Time Data Streaming
* Customer Lifetime Value Analytics
* Recommendation System
* Predictive Sales Forecasting
* Docker Deployment

---

## Author

Rahul Karmakar
M.Sc Physics (Astrophysics)
PGCP-BDA, C-DAC Chennai 

