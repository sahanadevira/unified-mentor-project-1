# ==========================================
# CUSTOMER, PRODUCT, AND PROFITABILITY
# PERFORMANCE ANALYSIS IN SUPPLY CHAIN OPERATIONS
# ==========================================

# ==========================================
# CELL 1 - IMPORT LIBRARIES
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10,5)

# ==========================================
# CELL 2 - LOAD DATASET
# ==========================================

df = pd.read_csv('/content/DataCoSupplyChainDataset.csv', encoding='latin1')

# If using Excel:
# df = pd.read_excel('/content/DataCoSupplyChainDataset.xlsx')

# ==========================================
# CELL 3 - DATASET OVERVIEW
# ==========================================

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

# ==========================================
# CELL 4 - MISSING VALUES
# ==========================================

print("Missing Values:")
print(df.isnull().sum())

# ==========================================
# CELL 5 - DATA CLEANING
# ==========================================

df = df.drop_duplicates()

print("Dataset Shape After Removing Duplicates:")
print(df.shape)

# ==========================================
# CELL 6 - TOTAL REVENUE, PROFIT, MARGIN
# ==========================================

total_revenue = df['Sales'].sum()

total_profit = df['Order Profit Per Order'].sum()

profit_margin = (total_profit / total_revenue) * 100

print("Total Revenue =", total_revenue)
print("Total Profit =", total_profit)
print("Profit Margin (%) =", round(profit_margin,2))

# ==========================================
# CELL 7 - TOP CATEGORIES BY SALES
# ==========================================

top_categories = (
    df.groupby('Category Name')['Sales']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_categories)

top_categories.plot(kind='bar')

plt.title('Top 10 Categories By Sales')
plt.xlabel('Category')
plt.ylabel('Sales')

plt.show()

# ==========================================
# CELL 8 - CATEGORY PROFITABILITY
# ==========================================

category_profit = (
    df.groupby('Category Name')['Order Profit Per Order']
      .sum()
      .sort_values(ascending=False)
)

print(category_profit.head(10))

category_profit.head(10).plot(kind='bar')

plt.title('Top Categories By Profit')
plt.xlabel('Category')
plt.ylabel('Profit')

plt.show()

# ==========================================
# CELL 9 - TOP CUSTOMERS
# ==========================================

top_customers = (
    df.groupby('Customer Id')['Order Profit Per Order']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_customers)

top_customers.plot(kind='bar')

plt.title('Top 10 Customers By Profit')
plt.xlabel('Customer ID')
plt.ylabel('Profit')

plt.show()

# ==========================================
# CELL 10 - DISCOUNT IMPACT ANALYSIS
# ==========================================

discount_profit = df[
    ['Order Item Discount Rate',
     'Order Item Profit Ratio']
]

print(discount_profit.corr())

plt.scatter(
    df['Order Item Discount Rate'],
    df['Order Item Profit Ratio']
)

plt.title('Discount vs Profit Ratio')
plt.xlabel('Discount Rate')
plt.ylabel('Profit Ratio')

plt.show()

# ==========================================
# CELL 11 - MARKET ANALYSIS
# ==========================================

market_profit = (
    df.groupby('Market')['Order Profit Per Order']
      .sum()
      .sort_values(ascending=False)
)

print(market_profit)

market_profit.plot(kind='bar')

plt.title('Profit By Market')
plt.xlabel('Market')
plt.ylabel('Profit')

plt.show()

# ==========================================
# CELL 12 - REGION ANALYSIS
# ==========================================

region_profit = (
    df.groupby('Order Region')['Order Profit Per Order']
      .sum()
      .sort_values(ascending=False)
)

print(region_profit.head(10))
region_profit.head(10).plot(kind='bar')

plt.title('Top Regions By Profit')
plt.xlabel('Region')
plt.ylabel('Profit')

plt.show()

# ==========================================
# CELL 13 - CUSTOMER SEGMENT ANALYSIS
# ==========================================

segment_profit = (
    df.groupby('Customer Segment')['Order Profit Per Order']
      .sum()
      .sort_values(ascending=False)
)

print(segment_profit)

segment_profit.plot(kind='bar')

plt.title('Customer Segment Profitability')
plt.xlabel('Customer Segment')
plt.ylabel('Profit')

plt.show()

# ==========================================
# CELL 14 - FINAL INSIGHTS
# ==========================================

print("PROJECT INSIGHTS")

print("1. Revenue and profit were successfully analyzed.")
print("2. Product categories contribute differently to sales and profits.")
print("3. A small group of customers generates a significant share of profits.")
print("4. Discounts impact profit margins.")
print("5. Market and regional profitability vary significantly.")
print("6. Data-driven decision making can improve business performance.")
