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