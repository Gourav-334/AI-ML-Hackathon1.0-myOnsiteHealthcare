import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle

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
