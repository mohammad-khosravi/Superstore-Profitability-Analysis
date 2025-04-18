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