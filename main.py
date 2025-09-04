import pandas as pd

# Extract: read CSV
df = pd.read_csv("sample_data.csv")
print("Data shape:", df.shape)
print(df.head())
