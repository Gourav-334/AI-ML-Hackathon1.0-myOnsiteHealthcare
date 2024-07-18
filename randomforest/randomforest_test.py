import pandas as pd
import joblib

# Load the saved model
loaded_model = joblib.load('randomforest\covid_outbreak_classifier.pkl')

# Example new data for prediction (single day data)
new_data = pd.DataFrame({
    'Confirmed': [20357],           # Replace with actual value
    'Deaths': [2000],                # Replace with actual value
    'Recovered': [300],            # Replace with actual value
    'Temparature (°C)': [34],      # Replace with actual value
    'Humidity (%)': [90]           # Replace with actual value
})

# Make prediction
prediction = loaded_model.predict(new_data)

# Interpret prediction
if prediction[0] == 1:
    print("Outbreak is likely.")
else:
    print("No outbreak predicted.")
