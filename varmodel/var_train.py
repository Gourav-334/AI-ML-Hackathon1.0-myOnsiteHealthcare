import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR
from sklearn.metrics import mean_squared_error
import pickle

# Load the data from Excel file
file_path = 'covid_Dataset1.xlsx'
df = pd.read_excel(file_path)

# Ensure the Date column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Setting the date as the index and setting the frequency
df.set_index('Date', inplace=True)
df = df.asfreq('D')

# Filling missing values in Recovered column with 0
df['Recovered'].fillna(0, inplace=True)

# Calculating daily increases
df['Daily Confirmed'] = df['Confirmed'].diff().fillna(df['Confirmed'])
df['Daily Deaths'] = df['Deaths'].diff().fillna(df['Deaths'])
df['Daily Recovered'] = df['Recovered'].diff().fillna(df['Recovered'])

# Ensure temperature and humidity columns exist and fill any missing values if necessary
df['Temparature (°C)'].ffill(inplace=True)
df['Humidity (%)'].ffill(inplace=True)

# Ensure all relevant columns are of type float
df['Confirmed'] = df['Confirmed'].astype(float)
df['Temparature (°C)'] = df['Temparature (°C)'].astype(float)
df['Humidity (%)'] = df['Humidity (%)'].astype(float)

# Splitting data into training and testing sets (80% train, 20% test)
train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]

# Selecting the features for the model
features = ['Confirmed', 'Temparature (°C)', 'Humidity (%)']

# Fitting the VAR model and automatically selecting the best lag order
model = VAR(train[features])
lag_order = model.select_order(maxlags=10)
best_lag = lag_order.aic

fit = model.fit(best_lag)

# Save the model to a file
with open('var_model.pkl', 'wb') as f:
    pickle.dump(fit, f)

# Making predictions
predictions = fit.forecast(train[features].values[-best_lag:], steps=len(test))
predictions_df = pd.DataFrame(predictions, index=test.index, columns=features)

# Calculating the mean squared error for confirmed cases
mse = mean_squared_error(test['Confirmed'], predictions_df['Confirmed'])
rmse = np.sqrt(mse)

# Predicting future values
future_days = 30  # Number of days to predict into the future
future_predictions = fit.forecast(train[features].values[-best_lag:], steps=future_days)
future_predictions_df = pd.DataFrame(future_predictions, index=pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=future_days, freq='D'), columns=features)

# Finding the predicted outbreak date
threshold = train['Confirmed'].max() * 1.2  # Define a threshold as 20% increase over the max of training data
future_confirmed = future_predictions_df['Confirmed']
outbreak_dates = future_confirmed[future_confirmed > threshold].index

if not outbreak_dates.empty:
    outbreak_date = outbreak_dates[0]
else:
    outbreak_date = "No outbreak date within prediction period"

# Print model summary, RMSE, and outbreak date
print(fit.summary())
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
axs[3].plot(future_predictions_df.index, future_predictions_df['Confirmed'], marker='o', linestyle='-', color='purple', label='Future Predictions')
if isinstance(outbreak_date, str):
    axs[3].text(0.5, 0.5, outbreak_date, transform=axs[3].transAxes, fontsize=12, color='red', verticalalignment='center', horizontalalignment='center')
else:
    axs[3].axvline(outbreak_date, color='red', linestyle='--', label='Predicted Outbreak Date')
axs[3].set_title('Future Predictions of Confirmed Cases')
axs[3].set_xlabel('Date')
axs[3].set_ylabel('Number of Confirmed Cases')
axs[3].legend()
axs[3].grid(True)

plt.tight_layout()
plt.show()
