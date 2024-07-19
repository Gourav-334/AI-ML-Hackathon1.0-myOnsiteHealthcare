import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error




#def var_test():
print("########################################################")

# Load the saved model
with open('var_model.pkl', 'rb') as f:
    saved_model = pickle.load(f)

# Load the new data from a different Excel file
new_file_path = 'covid_Dataset.xlsx'
new_df = pd.read_excel(new_file_path)

# Ensure the Date column is in datetime format
new_df['Date'] = pd.to_datetime(new_df['Date'], format='%d-%m-%Y')

# Setting the date as the index and setting the frequency
new_df.set_index('Date', inplace=True)
new_df = new_df.asfreq('D')

# Filling missing values in Recovered column with 0
new_df['Recovered'].fillna(0, inplace=True)

# Calculating daily increases
new_df['Daily Confirmed'] = new_df['Confirmed'].diff().fillna(new_df['Confirmed'])
new_df['Daily Deaths'] = new_df['Deaths'].diff().fillna(new_df['Deaths'])
new_df['Daily Recovered'] = new_df['Recovered'].diff().fillna(new_df['Recovered'])

# Ensure temperature and humidity columns exist and fill any missing values if necessary
new_df['Temparature (°C)'].ffill(inplace=True)
new_df['Humidity (%)'].ffill(inplace=True)

# Ensure all relevant columns are of type float
new_df['Confirmed'] = new_df['Confirmed'].astype(float)
new_df['Temparature (°C)'] = new_df['Temparature (°C)'].astype(float)
new_df['Humidity (%)'] = new_df['Humidity (%)'].astype(float)

# Selecting the features for the model
features = ['Confirmed', 'Temparature (°C)', 'Humidity (%)']

# Extracting the last known values to start the prediction
last_known_values = new_df[features].values[-saved_model.k_ar:]

# Making predictions
future_days = 30  # Number of days to predict into the future
predictions = saved_model.forecast(last_known_values, steps=future_days)
predictions_df = pd.DataFrame(predictions, index=pd.date_range(start=new_df.index[-1] + pd.Timedelta(days=1), periods=future_days, freq='D'), columns=features)

# Predicting the outbreak date
outbreak_threshold = 100
predictions_df['Daily Confirmed'] = predictions_df['Confirmed'].diff().fillna(predictions_df['Confirmed'])
outbreak_date = predictions_df[predictions_df['Daily Confirmed'] > outbreak_threshold].index[0]
print("Predicted Outbreak Date:", outbreak_date)

# Calculating the mean squared error for confirmed cases (if the new data contains actual future values)
if 'Confirmed' in new_df.columns and len(new_df) > len(last_known_values):
    actual_confirmed = new_df['Confirmed'].iloc[-future_days:]
    predicted_confirmed = predictions_df['Confirmed']
    mse = mean_squared_error(actual_confirmed, predicted_confirmed)
    rmse = np.sqrt(mse)
    print("Mean Squared Error:", mse)
    print("Root Mean Squared Error:", rmse)

# Plotting the future predictions
plt.figure(2, figsize=(12, 6))
plt.plot(new_df.index, new_df['Confirmed'], marker='o', linestyle='-', label='Actual Confirmed Cases')
plt.plot(predictions_df.index, predictions_df['Confirmed'], marker='o', linestyle='-', color='purple', label='Future Predictions')
plt.axvline(x=outbreak_date, color='red', linestyle='--', linewidth=1.5, label='Predicted Outbreak Date')
plt.title('Future Predictions of Confirmed Cases')
plt.xlabel('Date')
plt.ylabel('Number of Confirmed Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()










# predict_date()
# randomforest_outbreakdays()
# var_test()