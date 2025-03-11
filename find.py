import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('vehicles_data.csv')

# Get unique values of the "speed" column

print(df['t'].max())