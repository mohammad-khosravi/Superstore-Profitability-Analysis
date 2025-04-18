# Superstore Sales Insights & Profitability Analysis

Goal: To identify key areas of improvement within this company.
Techniques: EDA, data visualization, aggregation, pandas, matplotlib, seaborn
Dataset: https://public.tableau.com/app/learn/sample-data

First things first, let’s 

1. **Load and preview the dataset.**
2. **Check for missing values and data types.**
3. **Begin summarizing key sales and profit metrics.**

Let’s start by loading and inspecting the first few rows.

```python
# Load the CSV file
csv_path = "/mnt/data/sample_-_superstore.csv"
df = pd.read_csv(csv_path)

# Show basic info and the first few rows
df.info(), df.head()
```

### Next Steps

Let’s start identifying improvement opportunities by answering questions like:

1. **Which categories or sub-categories generate the most/least profit?**
2. **Are there any regions consistently underperforming?**
3. **Is discounting helping or hurting profitability?**
4. **Which customer segments are the most valuable?**

I’ll begin with a **summary of Sales and Profit by Category and Sub-Category**.

```python
import pandas as pd

# Load the dataset (update path as needed)
df = pd.read_csv('sample_-_superstore.csv')

# Group by Category and Sub-Category, then sum Sales and Profit
category_summary = df.groupby(['Category', 'Sub-Category'])[['Sales', 'Profit']].sum()

# Sort by Profit in descending order
category_summary = category_summary.sort_values(by='Profit', ascending=False)

# Round for better readability
category_summary = category_summary.round(2)

# Display the result
print(category_summary)
```

| Category | Sub-Category | Sales | Profit |
| --- | --- | --- | --- |
| Technology | Copiers | 149528.03 | 55617.82 |
| Technology | Phones | 330007.05 | 44515.73 |
| Technology | Accessories | 167380.32 | 41936.64 |
| Office Supplies | Paper | 78479.21 | 34053.57 |
| Office Supplies | Binders | 203412.73 | 30221.76 |
| Furniture | Chairs | 328449.1 | 26590.17 |
| Office Supplies | Storage | 223843.61 | 21278.83 |
| Office Supplies | Appliances | 107532.16 | 18138.01 |
| Furniture | Furnishings | 91705.16 | 13059.14 |
| Office Supplies | Envelopes | 16476.4 | 6964.18 |
| Office Supplies | Art | 27118.79 | 6527.79 |
| Office Supplies | Labels | 12486.31 | 5546.25 |
| Technology | Machines | 189238.63 | 3384.76 |
| Office Supplies | Fasteners | 3024.28 | 949.52 |
| Office Supplies | Supplies | 46673.54 | -1189.1 |
| Furniture | Bookcases | 114880 | -3472.56 |
| Furniture | Tables | 206965.53 | -17725.48 |

Now let’s plot it:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (adjust path if needed)
df = pd.read_csv('sample_-_superstore.csv')

# Group by Category and Sub-Category, summing the Profit
profit_data = df.groupby(['Category', 'Sub-Category'])['Profit'].sum().sort_values()

# Plot horizontal bar chart
plt.figure(figsize=(12, 8))
profit_data.plot(kind='barh', color='skyblue')
plt.title('Profitability by Category and Sub-Category')
plt.xlabel('Total Profit')
plt.ylabel('Sub-Categories (within Categories)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```
![Profitability By Category And Sub-Category](https://github.com/user-attachments/assets/183e0582-a495-4738-83e8-55a01101bcc7)


Here’s a breakdown of **sales and profit by Category and Sub-Category**. This highlights which product areas are driving or draining profitability.

### Key Observations:

- **Most Profitable Categories:**
    - Technology leads with Copiers ($55.6K), Phones ($44.5K), and Accessories ($41.9K)
    - Office Supplies follows with Paper ($34K) and Binders ($30.2K)
- **Least Profitable/Loss-Making Categories:**
    - Furniture shows poor performance, particularly Tables (-$17.7K) and Bookcases (-$3.4K)
    - Office Supplies "Supplies" category shows minor losses (-$1.1K)

### Conclusion:

The data suggests the company should focus on expanding their technology offerings while potentially restructuring or reviewing their furniture line, especially tables and bookcases, which are significantly impacting overall profitability.

Now let’s answer to the second question:

### Are there any regions consistently underperforming?

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (adjust path if needed)
df = pd.read_csv('sample_-_superstore.csv')

# Group by Region and summarize Sales and Profit
region_summary = df.groupby('Region')[['Sales', 'Profit']].sum().sort_values(by='Profit', ascending=False).round(2)

# Plotting Profit by Region
plt.figure(figsize=(8, 6))
region_summary['Profit'].plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Profit by Region')
plt.xlabel('Region')
plt.ylabel('Total Profit')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Optional: print the table
print(region_summary)
```
![Profit by Region](https://github.com/user-attachments/assets/29145a72-2f12-4cd2-90c4-94fe5f09c566)


Here’s the chart showing **Profit by Region**, along with the total Sales and Profit values.

### Key Observations:

- There's a significant performance gap between the top two regions (West and East) and the bottom two (South and Central)
- The West region generates more than twice the profit of the Central region, suggesting potential for improvement in underperforming areas

### Conclusion:

All regions are profitable, but the substantial variation indicates opportunities for standardizing best practices from the top-performing regions

The the next question:

### Is discounting helping or hurting profitability?

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('sample_-_superstore.csv')

# Scatter plot of Discount vs Profit
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', alpha=0.6)
plt.title('Impact of Discount on Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Bin discounts and calculate average profit per bin
discount_bins = pd.cut(df['Discount'], bins=[-0.01, 0, 0.1, 0.2, 0.3, 0.5, 1.0])
discount_summary = df.groupby(discount_bins)['Profit'].mean().round(2)

print(discount_summary)
```

![Impact Of Discount On Profit](https://github.com/user-attachments/assets/c91b9bc2-3bdb-4d11-9d8b-cbd5505cabc7)

### Key Observations:

1. **At 0% Discount** (left side of the plot):
    - The **majority of points are above the zero line**, indicating **positive profits**.
    - These are likely full-margin sales.
2. **0.1–0.2 Range**:
    - Still profitable in many cases, though a few sales start dipping into losses.
3. **Beyond 0.2 (20%)**:
    - A growing cluster of **negative-profit points**, especially between **0.3 and 0.5 (30–50%)**.
    - This suggests that heavy discounting is often unprofitable.
4. **At 50%+ Discounts**:
    - Most points are **below zero**, showing **significant losses**.
    - This is the danger zone — discounts this steep are hurting the business.
5. **By Category**:
    - The impact varies a bit by category:
        - **Technology** tends to remain more profitable even with some discounting.
        - **Furniture** and **Office Supplies** seem more sensitive to high discounts.

### Conclusion:

Discounting starts hurting profitability significantly beyond 20%, with most losses concentrated in the 30–50% range. Businesses should reconsider deep discounts unless they're strategic (e.g., clearance). Keeping discounts below 10–20% generally supports profitability.

Now the last question:

### Which customer segments are the most valuable?

```python
# Re-import required libraries due to code execution state reset
import pandas as pd
import matplotlib.pyplot as plt

# Reload the dataset
csv_path = "sample_-_superstore.csv"
df = pd.read_csv(csv_path)

# Group by Segment and calculate total Sales and Profit
segment_summary = df.groupby('Segment')[['Sales', 'Profit']].sum().sort_values(by='Profit', ascending=False).round(2)

# Plotting Profit by Customer Segment
plt.figure(figsize=(8, 6))
segment_summary['Profit'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Profit by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Total Profit')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print(segment_summary)
```

![Profit By Customer Segment](https://github.com/user-attachments/assets/f5a788a8-a920-4ad5-98cf-4c05146e19be)


### Key Observations:

| Segment | Total Sales | Total Profit |
| --- | --- | --- |
| **Consumer** | $1,161,401 | $134,119 |
| **Corporate** | $706,146 | $91,979 |
| **Home Office** | $429,653 | $60,299 |
- **Consumer** segment is the most valuable — it generates the **highest sales and profit**.
- **Corporate** comes second, followed by **Home Office**.

### Conclusion:

While all segments are profitable, the **Consumer segment** drives the largest share of business performance.

### Key Insights:

| Segment | Total Sales | Total Profit |
| --- | --- | --- |
| **Consumer** | $1,161,401 | $134,119 |
| **Corporate** | $706,146 | $91,979 |
| **Home Office** | $429,653 | $60,299 |

---

### Interpretation:

- **Consumer** segment is the most valuable — it generates the **highest sales and profit**.
- **Corporate** comes second, followed by **Home Office**.
- While all segments are profitable, the **Consumer segment** drives the largest share of business performance.
