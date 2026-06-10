# E-Commerce Big Data Analytics Pipeline

## Overview

A scalable end-to-end Big Data Analytics platform built using Apache Hadoop, Apache Spark, Apache Hive, Apache Kafka, and Streamlit.

The project simulates a real-world e-commerce environment by generating large-scale transactional data, storing it in a distributed Hadoop ecosystem, processing it through Spark, performing analytical transformations using Hive and Spark SQL, and visualizing insights through an interactive Streamlit dashboard.

The platform supports both batch analytics and real-time streaming analytics.

---

## Architecture

```text
Synthetic Data Generation
          ↓
   Apache Kafka
          ↓
Spark Structured Streaming
          ↓
    Hadoop HDFS
          ↓
    Hive Metastore
          ↓
   KPI Aggregations
          ↓
 Streamlit Dashboard
```

---

## Features

### Batch Analytics

* Generated 1,000,000+ synthetic e-commerce transactions
* Distributed storage using Hadoop HDFS
* Spark ETL pipeline for large-scale data processing
* Hive-based analytical queries
* Business KPI generation

### Real-Time Streaming Analytics

* Kafka-based event streaming
* Spark Structured Streaming consumer
* Live KPI computation
* Revenue aggregation by category
* Revenue aggregation by payment method
* Order status monitoring
* Orders-per-minute tracking
* Streaming KPI storage in HDFS

### Dashboard

* Interactive Streamlit dashboard
* Revenue analysis
* Product performance tracking
* Customer analytics
* Payment insights
* Auto-refreshing visualizations

---

## Tech Stack

### Big Data

* Apache Hadoop HDFS
* Apache Spark 3.5
* Apache Hive
* Apache Kafka
* Apache ZooKeeper

### Analytics

* PySpark
* Spark SQL
* HiveQL

### Visualization

* Streamlit
* Plotly
* Pandas

### Programming

* Python 3

---

## Dataset

Synthetic dataset generated using Faker and custom business logic.

### Data Scale

| Dataset   | Records    |
| --------- | ---------- |
| Customers | 100,000    |
| Products  | 10,000     |
| Orders    | 1,000,000+ |
| Payments  | 1,000,000+ |

---

## Real-Time KPIs

The streaming layer computes the following KPIs in near real-time:

### Revenue by Category

* Electronics
* Fashion
* Grocery
* Beauty
* Sports
* Books
* Home

### Revenue by Payment Method

* UPI
* Credit Card
* Debit Card
* Net Banking

### Order Status Distribution

* Delivered
* Returned
* Cancelled

### Orders per Minute

Live throughput monitoring using Spark Structured Streaming.

---

## Dashboard for Visualization

Streamlit Dashboard:

**Deployment Link:** Coming Soon

(Currently running locally using Streamlit)

---

## Running the Project

### Start Hadoop Services

```bash
start-dfs.sh
start-yarn.sh
```

### Start Kafka

```bash
zookeeper-server-start.sh config/zookeeper.properties

kafka-server-start.sh config/server.properties
```

### Start Producer

```bash
python producer.py
```

### Start Streaming Analytics

```bash
spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 \
stream_kpis.py
```

### Launch Dashboard

```bash
streamlit run app.py
```

---

## Key Learnings

* Distributed storage using Hadoop HDFS
* Batch and streaming data processing with Apache Spark
* Kafka-based event-driven architectures
* Hive data warehousing concepts
* Building real-time analytical dashboards
* Data engineering workflow design
* End-to-end analytics pipeline development

---

## Future Enhancements

* Cloud deployment on AWS
* Docker containerization
* Airflow workflow orchestration
* CI/CD integration
* Real-time dashboard deployment
* Advanced customer segmentation
* Machine learning-based recommendations

---

## Author

Rahul Karmakar
M.Sc. Physics (Astrophysics) | PGCP Big Data Analytics



