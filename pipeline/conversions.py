import pickle
import json
import os
import pandas as pd
from statsmodels.tsa.api import VAR










# Conversion functions

def to_json(json_file, date, cell1, cell2, cell3):
	file = open(json_file, "a")

	file.write(f"{{\n\"Date\": \"{date}\",\n\"Confirmed\": {cell1},\n\"Recovered\": {cell2},\n\"Deceased\": {cell3}\n}}")
	file.write(",\n")



def csv_to_json(csv_file, json_file):
	print(f"Compiling \"{csv_file}\" to \"{json_file}\"...")

	data = pd.read_csv(csv_file)

	#print(type(data["Date"]))

	file = open(json_file, "a")
	#file.write("[\n")
	
	for i in range(0,500):
		the_date = data.at[i, "Date"]
		cell1 = data.at[i, "Confirmed"]
		cell2 = data.at[i, "Recovered"]
		cell3 = data.at[i, "Deceased"]

		# Conversion to JSON
		to_json(json_file, the_date, cell1, cell2, cell3)
	
	file.write("]")

	print(f"\"{csv_file}\" to \"{json_file}\" compilation completed!")










def predictVAR(csv_file, pickle_file, date_index):
    df = pd.read_csv(csv_file, parse_dates=['Date'])
    df = df.sort_values(by='Date')

    # Drop the 'Date' column as it's not used for training the VAR model
    data = df.drop(columns=['Date'])

    # Load the trained VAR model from the pickle file
    with open(pickle_file, 'rb') as f:
        loaded_model = pickle.load(f)

    # Define a function to make predictions for a given date index
    if date_index >= len(data) or date_index < loaded_model.k_ar:
        raise ValueError("Date index out of range or not enough lag values.")
    
    # Prepare the input data for prediction
    input_data = data.iloc[date_index - loaded_model.k_ar : date_index].values
    
    # Make prediction
    prediction = loaded_model.forecast(y=input_data, steps=1)
    
    # Return the predicted values
    predicted_confirmed, predicted_recovered, predicted_deceased = prediction[0]
    
    return {
        'Date': df.iloc[date_index]['Date'],
        'Confirmed': predicted_confirmed,
        'Recovered': predicted_recovered,
        'Deceased': predicted_deceased
    }



def insertCSV(csv_file, pickle_file):
	file = open(csv_file, "a")

	for i in range(500, 530):
		argument = predictVAR(csv_file, pickle_file, i)["Confirmed"] + "," + predictVAR(csv_file, i)["Recovered"] + "," + predictVAR(csv_file, i)["Deceased"]
		file.write(argument)










insertCSV("Gujarat.csv", "Gujarat_trained.pkl")