import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score










#def predict_date():
new_data = pd.read_excel('covid_Dataset3.xlsx')


# Ensure Date column is in datetime format
new_data['Date'] = pd.to_datetime(new_data['Date'])

# Set Date column as index
new_data.set_index('Date', inplace=True)

# Step 2: Load the saved ARIMA model from file
with open('arima_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Define outbreak threshold
outbreak_threshold = 10000  # Example threshold for outbreak

# Initialize forecast
forecast_steps = 1
forecast = loaded_model.forecast(steps=forecast_steps)
predicted_cases = forecast[-1]
print(predicted_cases)
# Continue forecasting until the threshold is met
while predicted_cases < outbreak_threshold:
    forecast_steps += 1
    forecast = loaded_model.forecast(steps=forecast_steps)
    predicted_cases = forecast[-1]

# Extract the predicted outbreak date
last_date = new_data.index[-1]
predicted_outbreak_date = pd.date_range(start=last_date, periods=forecast_steps + 1)[-1]

print(f'Predicted outbreak date: {predicted_outbreak_date.strftime("%Y-%m-%d")}')










#def randomforest_outbreakdays():
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
plt.figure(1, figsize=(10, 5))
plt.plot(y_test.values, label='Actual Outbreak Days')
plt.plot(predictions, label='Predicted Outbreak Days', linestyle='--')
plt.legend()
plt.title('Actual vs Predicted Outbreak Days')
plt.xlabel('Days')
plt.ylabel('Outbreak')
plt.show()
print("########################################################")










