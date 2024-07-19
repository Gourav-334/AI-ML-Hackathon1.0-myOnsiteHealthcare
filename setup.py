import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Function to run a CMD command
def run_cmd_command(command):
    try:
        # Running the command
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("Command output:", result.stdout)
        else:
            print("Error:", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")


run_cmd_command("python.exe -m pip install --upgrade pip")
run_cmd_command("pip install pandas")
run_cmd_command("pip install numpy")
run_cmd_command("pip install matplotlib")
run_cmd_command("pip install pandas numpy matplotlib statsmodels openpyxl")
run_cmd_command("pip install statsmodels")