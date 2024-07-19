import pandas as pd
from statsmodels.tsa.api import VAR
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error



# Load your data
file_path = "C:\\Users\\91966\\OneDrive\\Desktop\\Instant Codes\\Cloned Repositaries\\Machine-Learning-Experiments\\pipeline\\GujaratFinal.xlsx"
data = pd.read_excel(file_path)

# Fill NaN values in the 'Tested' column with 0
data['Tested'] = data['Tested'].fillna(0)

# Set 'Date' column as the index
data.set_index('Date', inplace=True)

# Ensure the data is in datetime format if 'Date' is not already in datetime
data.index = pd.to_datetime(data.index)

# Split the data into training and testing sets (70:30 ratio)
train_data, test_data = train_test_split(data, test_size=0.3, shuffle=False)

# Fit the VAR model on the training data
model = VAR(train_data)
fitted_model = model.fit(maxlags=15, ic='aic')

lag_order = fitted_model.k_ar
forecast_input = train_data.values[-lag_order:]
forecast = fitted_model.forecast(y=forecast_input, steps=len(test_data))

# Convert forecasted values to a DataFrame for comparison
forecast_data = pd.DataFrame(forecast, index=test_data.index, columns=data.columns)

mse = mean_squared_error(test_data, forecast_data)
mae = mean_absolute_error(test_data, forecast_data)
print("Mean squared error: ", mse)
print("Mean absolute error: ", mae)

# Save the training data to a pickle file
with open('train_data.pkl', 'wb') as file:
    pickle.dump(train_data, file)

# Print the training data and a summary of the model
print("Training Data:")
print(train_data.head(10))

print("\nModel Summary:")
print(fitted_model.summary())

# Rishab, its on you...
#print(accuracy_score(y_test, y_pred))