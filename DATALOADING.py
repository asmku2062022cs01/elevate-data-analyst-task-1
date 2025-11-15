#Import Libraries & Load Dataset
import pandas as pd
#import numpy as np

# CSV load (YOUR FILE NAME HERE)
df = pd.read_csv("Mall_Customers1.csv")

# Keep copy of original
df_original = df.copy()



# 2) Basic Info

print("Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe(include='all'))



# 3) Clean Column Names

df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]



# 4) Remove Duplicates

print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)



# 5) Missing Values Handling

missing = df.isnull().sum()
print("Missing values:\n", missing)

# Drop columns with more than 50% missing
df = df.dropna(axis=1, thresh=len(df)*0.5)

# Fill numerical missing values with median
num_cols = df.select_dtypes(include=['number']).columns
for c in num_cols:
    df[c] = df[c].fillna(df[c].median())

# Fill categorical missing values with mode
cat_cols = df.select_dtypes(include=['object']).columns
for c in cat_cols:
    df[c] = df[c].fillna(df[c].mode()[0])



# 6) Standardize Text Columns

for c in cat_cols:
    df[c] = df[c].astype(str).str.lower().str.strip()



# 7) Convert Date Columns (if any)

# Example: if dataset has 'join_date'
if 'join_date' in df.columns:
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')



# 8) Fix Data Types

if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

if 'annual_income_(k$)' in df.columns:
    df['annual_income_(k$)'] = pd.to_numeric(df['annual_income_(k$)'], errors='coerce')

if 'spending_score_(1-100)' in df.columns:
    df['spending_score_(1-100)'] = pd.to_numeric(df['spending_score_(1-100)'], errors='coerce')



# 9) Outlier Treatment for Numerical Columns

for col in num_cols:
    lower = df[col].quantile(0.01)
    upper = df[col].quantile(0.99)
    df[col] = df[col].clip(lower, upper)



# 10) Create New Features (Optional)

if 'age' in df.columns:
    df['age_group'] = pd.cut(
        df['age'], 
        bins=[0, 18, 30, 45, 60, 120],
        labels=["<18", "18-30", "30-45", "45-60", "60+"]
    )



# 11) Final Data Quality Checks
print("Remaining missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df.describe())



# 12) Save Cleaned Dataset

df.to_csv("mall_customers_cleaned.csv", index=False)

print("Cleaning complete! File saved: mall_customers_cleaned.csv")
