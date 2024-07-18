import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error

# Load the data from Excel file
file_path = 'covid_Dataset1.xlsx'
df = pd.read_excel(file_path)

# Ensure the Date column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Setting the date as the index
df.set_index('Date', inplace=True)

# Filling missing values in Recovered column with 0
df['Recovered'].fillna(0, inplace=True)

# Calculating daily increases
df['Daily Confirmed'] = df['Confirmed'].diff().fillna(df['Confirmed'])
df['Daily Deaths'] = df['Deaths'].diff().fillna(df['Deaths'])
df['Daily Recovered'] = df['Recovered'].diff().fillna(df['Recovered'])

# Splitting data into training and testing sets (80% train, 20% test)
confirmed_cases = df['Confirmed']
train_size = int(len(confirmed_cases) * 0.8)
train, test = confirmed_cases[:train_size], confirmed_cases[train_size:]

# Fitting the Exponential Smoothing model
model = ExponentialSmoothing(train, trend='add', seasonal=None, seasonal_periods=None)
fit = model.fit()

# Making predictions
predictions = fit.forecast(len(test))

# Calculating the mean squared error
mse = mean_squared_error(test, predictions)
rmse = np.sqrt(mse)

# Predicting future values
future_days = 30  # Number of days to predict into the future
future_predictions = fit.forecast(future_days)

# Finding the predicted outbreak date
threshold = train.max() * 1.2  # Define a threshold as 20% increase over the max of training data
outbreak_date = future_predictions[future_predictions > threshold].index[0]

# Print model parameters, RMSE, and outbreak date
print("Model Parameters:\n", fit.params)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Predicted Outbreak Date:", outbreak_date)

# Plotting the trends for confirmed cases, deaths, and recoveries
fig, axs = plt.subplots(4, 1, figsize=(12, 24))

# Daily confirmed cases
axs[0].plot(df.index, df['Daily Confirmed'], marker='o', linestyle='-')
axs[0].set_title('Daily Confirmed Cases')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Number of Cases')
axs[0].grid(True)

# Daily deaths
axs[1].plot(df.index, df['Daily Deaths'], marker='o', linestyle='-', color='red')
axs[1].set_title('Daily Deaths')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Number of Deaths')
axs[1].grid(True)

# Daily recoveries
axs[2].plot(df.index, df['Daily Recovered'], marker='o', linestyle='-', color='green')
axs[2].set_title('Daily Recoveries')
axs[2].set_xlabel('Date')
axs[2].set_ylabel('Number of Recoveries')
axs[2].grid(True)

# Future predictions
axs[3].plot(df.index, df['Confirmed'], marker='o', linestyle='-', label='Actual Confirmed Cases')
axs[3].plot(pd.date_range(df.index[-1], periods=future_days, freq='D'), future_predictions, marker='o', linestyle='-', color='purple', label='Future Predictions')
axs[3].axvline(outbreak_date, color='red', linestyle='--', label='Predicted Outbreak Date')
axs[3].set_title('Future Predictions of Confirmed Cases')
axs[3].set_xlabel('Date')
axs[3].set_ylabel('Number of Confirmed Cases')
axs[3].legend()
axs[3].grid(True)

plt.tight_layout()
plt.show()
