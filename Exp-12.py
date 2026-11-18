import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

df = pd.read_csv("customer_churn.csv")

print(df.head())
print(df.info())
print(df.columns)

print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Mode:\n", df.mode().iloc[0])
print("Standard Deviation:\n", df.std(numeric_only=True))
print("Variance:\n", df.var(numeric_only=True))
print("Minimum:\n", df.min(numeric_only=True))
print("Maximum:\n", df.max(numeric_only=True))
print("Percentiles:\n", df.quantile([0.25, 0.50, 0.75], numeric_only=True))

df.select_dtypes(include="number").hist(figsize=(10, 8))
plt.show()

sns.boxplot(data=df.select_dtypes(include="number"))
plt.show()

num = df.select_dtypes(include="number")
if len(num.columns) >= 2:
    sns.scatterplot(x=num.columns[0], y=num.columns[1], data=df)
    plt.show()

sns.heatmap(num.corr(), annot=True, cmap="coolwarm")
plt.show()

print("Missing values:\n", df.isnull().sum())

df = df.dropna(how="all")
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
df = df.dropna()

num_cols = df.select_dtypes(include="number").columns
z_scores = df[num_cols].apply(zscore).abs()
outliers = (z_scores > 3).any(axis=1)

print("Outliers:\n", df[outliers])

df = df[~outliers]

print("Remaining missing values:\n", df.isnull().sum())
print("Cleaned dataset:\n", df)

df.to_csv("cleaned_customer_churn.csv", index=False)

print("Cleaned data saved successfully.")