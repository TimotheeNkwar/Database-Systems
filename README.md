# 1 🦷 Dentist Clinic Database

This project contains the design and implementation of a relational database system for a dental clinic. The goal is to efficiently manage data related to staff, patients, appointments, treatments, medicines, dentist, and payments.

## 🚀 Features

- Fully normalized to **Third Normal Form (3NF)** for data integrity
- Includes 8+ well-structured tables (Staff, Patients, Appointments, etc.)
- Supports data analysis for clinic performance insights
- Designed for scalability and real-world clinic management

## 🗃️ Key Tables

- `Staff`: Dentists, nurses, and admin employees
- `Patients`: Personal and medical information
- `Appointments`: Scheduling and history
- `Treatments` & `Operations`: Medical and surgical procedures
- `Medicines` & `Prescriptions`: Inventory and prescriptions
- `Payments`: Patient billing records

## 📊 Analytics Capabilities

- Identify top-performing dentists
- Track popular medicines
- Analyze payment trend

---



## 2 🧪 Demo: Combining SQLite3, Pandas, and Dask

This demo showcases how to integrate **SQLite3** with **Pandas** for initial data extraction and processing, and then scale up using **Dask** for efficient handling of larger datasets.

### 🔄 Workflow Overview

1. **SQLite3 + Pandas**  
   - Connect to a local SQLite database  
   - Run SQL queries to extract relevant data  
   - Load the results into a Pandas DataFrame for inspection or preprocessing

2. **Pandas ➜ Dask Transition**  
   - Convert Pandas DataFrames into Dask DataFrames  
   - Leverage Dask's parallel computing capabilities for scalable data manipulation

### ✅ Key Benefits

- Simple local database integration with SQLite
- Seamless transition from small-scale (Pandas) to large-scale (Dask) processing
- Ideal for data science workflows involving growing datasets

### 💻 Technologies Used

- `sqlite3` (Python standard library)
- `pandas`
- `dask`

---

This demo is useful for data professionals looking to bridge lightweight SQL databases with scalable Python analytics.

## 3 Benchmark Pandas vs Dask

This script compares the performance of simple operations (like summing a column)  
between two popular Python data processing libraries:

- **Pandas**: in-memory processing, ideal for small to medium datasets  
- **Dask**: parallel and lazy execution, suitable for larger datasets

The goal is to demonstrate execution time differences using `%timeit` in Python,  
highlighting the strengths and limitations of each library depending on data size.

---

## Contents

- Creating a sample DataFrame  
- Summing a column using Pandas and Dask  
- Measuring execution time with `%timeit`  
- Instructions for installing dependencies and running the benchmark

---

## Usage

```bash
pip install pandas dask matplotlib
jupyter notebook  # or python benchmark_pandas_dask.ipynb
