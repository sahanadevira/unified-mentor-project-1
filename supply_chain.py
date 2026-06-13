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
