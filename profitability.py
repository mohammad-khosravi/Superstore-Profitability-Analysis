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

