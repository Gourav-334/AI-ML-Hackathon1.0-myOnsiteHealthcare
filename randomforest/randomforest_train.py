import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import joblib

# Load the new data from a different Excel file
new_file_path = 'covid_Dataset.xlsx'
df = pd.read_excel(new_file_path, engine='openpyxl')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

# Impute missing values using forward fill
df['Recovered'] = df['Recovered'].ffill()

# Calculate daily increase in confirmed cases
df['Daily_Increase'] = df['Confirmed'].diff()

# Define outbreak: a day when the daily increase exceeds a certain threshold (e.g., 20% of previous day's cases)
threshold = 0.2
df['Outbreak'] = (df['Daily_Increase'] > df['Confirmed'].shift(1) * threshold).astype(int)

# Prepare features and target
features = ['Confirmed', 'Deaths', 'Recovered', 'Temparature (°C)', 'Humidity (%)']
X = df[features]
y = df['Outbreak']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize RandomForestClassifier
clf = RandomForestClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Evaluate the classifier
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Save the model to a file
model_filename = 'covid_outbreak_classifier.pkl'
joblib.dump(clf, model_filename)
print(f"Model saved as {model_filename}")
