import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle

# Step 1: Load the data from Excel
df = pd.read_excel('covid_Dataset3.xlsx')
print(df.columns)

# Step 2: Selecting relevant features and preparing data
features = ['Date', 'Confirmed', 'Deaths', 'Temparature (°C)', 'Humidity (%)']
df = df[features]


# Ensure Date column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set Date column as index for time series analysis
df.set_index('Date', inplace=True)

# Step 3: Fit an ARIMA model
model = ARIMA(df['Confirmed'], order=(5,1,0))  # Example order, tune based on your data
model_fit = model.fit()

# Step 4: Forecast only one step ahead (predicting outbreak date)
forecast = model_fit.forecast(steps=1)

# Extract the predicted date
predicted_date = forecast.index[0].strftime("%Y-%m-%d")
print(f'Predicted outbreak date: {predicted_date}')


with open('arima_model.pkl', 'wb') as f:
    pickle.dump(model_fit, f)

print("Model saved successfully.")
