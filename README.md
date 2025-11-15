# Mall Customers Data Cleaning & Preprocessing

## Task Description
This project involves cleaning and preprocessing the Mall Customers dataset. The main objectives are to handle missing values, remove duplicates, standardize text fields (like gender), fix data types, and prepare the dataset for analysis.

## Steps Performed
1. **Import Libraries & Load Dataset**: Loaded CSV file using Pandas.  
2. **Basic Data Inspection**: Checked shape, info, and summary statistics of the dataset.  
3. **Clean Column Names**: Renamed columns to lowercase and replaced spaces with underscores.  
4. **Remove Duplicates**: Identified and dropped duplicate rows.  
5. **Handle Missing Values**:  
   - Dropped columns with more than 50% missing values.  
   - Filled numerical missing values with median.  
   - Filled categorical missing values with mode.  
6. **Standardize Text Columns**: Converted text to lowercase and removed extra spaces.  
7. **Convert Date Columns**: Standardized date formats (if any).  
8. **Fix Data Types**: Ensured numeric and categorical columns have correct types.  
9. **Outlier Treatment**: Clipped numerical columns at 1st and 99th percentiles.  
10. **Feature Creation (Optional)**: Created an `age_group` column based on age ranges.  
11. **Final Data Quality Checks**: Verified no missing values or duplicates remain.  

## How to Run
- **Python script**: `python data_cleaning.py`  
- **Jupyter Notebook**: Open the notebook and run all cells.

## Outcome
- Cleaned dataset saved as `mall_customers_cleaned.csv`.  
- Data is ready for further analysis or modeling.

## GitHub Submission
- Commit your changes with a clear message, e.g., `Initial commit: data cleaning script and datasets`.  
- Copy your GitHub repository link and submit it using the required submission link.

