import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the new data from a different Excel file
new_file_path = 'covid_Dataset.xlsx'
df = pd.read_excel(new_file_path, engine='openpyxl')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

# Impute missing values using forward fill
df['Recovered'].fillna(method='ffill', inplace=True)

# Calculate daily increase in confirmed cases
df['Daily_Increase'] = df['Confirmed'].diff()

# Define outbreak: a day when the daily increase exceeds a certain threshold (e.g., 20% of previous day's cases)
threshold = 0.2
df['Outbreak'] = (df['Daily_Increase'] > df['Confirmed'].shift(1) * threshold).astype(int)

# Create rolling averages
df['Confirmed_MA7'] = df['Confirmed'].rolling(window=7).mean()
df['Deaths_MA7'] = df['Deaths'].rolling(window=7).mean()
df['Recovered_MA7'] = df['Recovered'].rolling(window=7).mean()

# Drop any rows with NaN values that may have resulted from rolling window calculations
df.dropna(inplace=True)

# Display the DataFrame with new features
print(df)

# Define features and target
features = ['Confirmed', 'Deaths', 'Recovered', 'Temparature (°C)', 'Humidity (%)', 'Confirmed_MA7', 'Deaths_MA7', 'Recovered_MA7', 'Daily_Increase']
target = 'Outbreak'

# Split the data into training and testing sets
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)
print(f'Accuracy: {accuracy}')
print(report)

# Plot actual vs predicted outbreak days
plt.figure(figsize=(10, 5))
plt.plot(y_test.values, label='Actual Outbreak Days')
plt.plot(predictions, label='Predicted Outbreak Days', linestyle='--')
plt.legend()
plt.title('Actual vs Predicted Outbreak Days')
plt.xlabel('Days')
plt.ylabel('Outbreak')
plt.show()
