import pandas as pd
from statsmodels.tsa.api import VAR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

# GujaratFinal.xlsx
file_path = "Gujarat.csv"
data = pd.read_csv(file_path)

# Set 'Date' as the index
data.set_index('Date', inplace=True)

# Ensure the data is in datetime format
data.index = pd.to_datetime(data.index)

# 'Confirmed' is the only dependent variable
data = data[['Confirmed', 'Recovered', 'Deceased']]

# 70:30 ratio splitting
train_data, test_data = train_test_split(data, test_size=0.3, shuffle=False)

# Model fitting on VAR regression
model = VAR(train_data)

# Time lags of 15 units, ic (information criterion) avoids overfitting
fitted_model = model.fit(maxlags=15, ic='aic')

# Gujarat_train_data.xlsx
with open('Gujarat_train_data.pkl', 'wb') as file:
    pickle.dump(train_data, file)

# Gujarat_fitted_model.xlsx
with open('Gujarat_fitted_model.pkl', 'wb') as file:
    pickle.dump(fitted_model, file)

# Make predictions on the test data
lag_order = fitted_model.k_ar
forecast_input = train_data.values[-lag_order:]
forecast = fitted_model.forecast(y=forecast_input, steps=len(test_data))

# Convert forecasted values to a DataFrame for comparison
forecast_df = pd.DataFrame(forecast, index=test_data.index, columns=test_data.columns)

# Calculate Mean Squared Error for the forecasts
mse = mean_squared_error(test_data, forecast_df)
print(f'Mean Squared Error: {mse}')


# Sample from training & summary
print("Training Data:")
print(train_data.head())

print("\nModel Summary:")
print(fitted_model.summary())
