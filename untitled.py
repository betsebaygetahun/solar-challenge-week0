import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/ethiopia_solar.csv")

df.head()
# Summary of numeric columns
df.describe()
# Count missing values
missing_values = df.isna().sum().sort_values(ascending=False)
print("Missing values per column:\n", missing_values)

# Percentage of missing values
missing_percent = (df.isna().mean() * 100).round(2)
print("\nPercentage of missing values:\n", missing_percent)

# List columns with >5% missing values
columns_with_nulls = missing_percent[missing_percent > 5]
print("\nColumns with >5% missing values:\n", columns_with_nulls)
# Drop or fill missing values depending on analysis
df_clean = df.dropna(subset=columns_with_nulls.index)
# OR: df.fillna(df.median(), inplace=True)
