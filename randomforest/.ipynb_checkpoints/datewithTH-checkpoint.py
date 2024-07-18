import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the new data from a different Excel file
new_file_path = 'covid_Dataset1.xlsx'
df = pd.read_excel(new_file_path, engine='openpyxl')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

# Impute missing values using forward fill
df['Recovered'] = df['Recovered'].ffill()

# Calculate daily increase in confirmed cases
df['Daily_Increase'] = df['Confirmed'].diff()

# Define outbreak: a day when the daily increase exceeds a certain threshold (e.g., 20% of previous day's cases)
threshold = 0.2
df['Outbreak'] = (df['Daily_Increase'] > df['Confirmed'].shift(1) * threshold).astype(int)

# Find the first outbreak date
outbreak_date = df.loc[df['Outbreak'] == 1, 'Date'].min()

print(f"The outbreak date is: {outbreak_date}")

# Plotting (optional)
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Daily_Increase'], label='Daily Increase')
plt.axvline(outbreak_date, color='r', linestyle='--', label=f'Outbreak Date: {outbreak_date.date()}')
plt.legend()
plt.title('Daily Increase in Confirmed Cases with Outbreak Date')
plt.xlabel('Date')
plt.ylabel('Daily Increase')
plt.show()
