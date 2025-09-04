import pandas as pd

# Extract: read CSV
df = pd.read_csv("sample_data.csv")
print("Data shape:", df.shape)
print(df.head())

# Drop nulls
df = df.dropna()

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Rename columns
df = df.rename(columns={"old_col": "new_col"})

# Add new column
df["total_price"] = df["quantity"] * df["unit_price"]

print(df.head())


from sqlalchemy import create_engine

# Create DB connection (replace with your creds)
engine = create_engine("postgresql://etl_user:etl_pass123@localhost:5432/etl_project")

# Load DataFrame into table
df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Data loaded successfully into PostgreSQL!")

