import pickle
import json
import os
import pandas as pd










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










csv_to_json("Ahmedabad.csv", "Ahmedabad.json")
csv_to_json("Amreli.csv", "Amreli.json")
csv_to_json("Anand.csv", "Anand.json")
csv_to_json("Aravali.csv", "Aravali.json")
csv_to_json("Baruch.csv", "Baruch.json")
csv_to_json("Bhavnagar.csv", "Bhavnagar.json")
csv_to_json("Dahod.csv", "Dahod.json")
csv_to_json("Gandhinagar.csv", "Gandhinagar.json")
csv_to_json("Gujarat.csv", "Gujarat.json")