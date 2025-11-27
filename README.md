# Mall Customer Segmentation – Data Cleaning & Summary

## 📌 Project Overview
The goal of this task is to clean the **Mall Customers dataset (Mall_Customers4.csv)** by handling missing values, removing duplicates, fixing column formatting, converting datatypes, and generating a summary of the dataset.

---

## 🧾 Steps I Completed
1. Loaded dataset using pandas
2. Cleaned column names (removed spaces + lowercased)
3. Handled missing values:
   - Filled missing Gender with "Female"
   - Filled missing Age with 30
   - Filled missing Spending Score with 72
   - Filled missing Annual Income with column median
   - Filled missing CustomerID with next available ID
4. Removed unwanted column (`Unnamed: 5`)
5. Removed duplicate records
6. Converted `date` column to datetime format
7. Generated dataset summary (total rows, missing values per column, removed duplicates, datatypes)

---

## Dataset Summary (After Cleaning)
| Metric | Result |
|--------|--------|
| Total rows | 201 |
| Missing values | 0 across all columns |
| Duplicates removed | 0 |
| Date column format | Converted to datetime |

---
project-folder/
│── Mall_Customers4.CSV
│── notebook.ipynb (or .py script)
│── PDF
│── README.md

