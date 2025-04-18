import pandas as pd

# Load the CSV file
csv_path = "sample_-_superstore.csv"
df = pd.read_csv(csv_path)

# Show basic info and the first few rows
df.info()
print(df.head())