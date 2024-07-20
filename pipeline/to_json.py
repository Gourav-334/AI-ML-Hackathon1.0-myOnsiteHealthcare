import pickle
import json
import os
import pandas as pd



def csv_to_json(csv_file, json_file):
	data = pd.read_csv(csv_file)

	file = open(json_file, "a")
	file.write(data.to_json())



csv_to_json("Gujarat.csv", "Gujarat.json")