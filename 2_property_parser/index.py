# -*- coding: utf-8 -*-
"""
Module to iterate files in a folder and returns a dataframe/excel file of supercapacitor properties.

"""
import properties as pr
import pandas as pd
import os
import json
import numpy as np

# Path to the abstract folder
folder_path = ".\\abstract"  # Replace with the path to your folder

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Data Frame to store the property values extracted in respective property columns
df = pd.DataFrame(columns=['EID','Specific Capacitance', 
                                        'Surface Area','Energy Density', 'Power Density',
                                        'Voltage','Current Density','Cycles'])

# Iterate over each file in the folder
for file_name in file_list:
    

    if file_name.endswith(".txt"):  # Process only text files
        file_path = os.path.join(folder_path, file_name)  # Get the full file path

        with open(file_path, "r", encoding="utf8") as file:
            content = file.read()
            all_prop = [file_name]            
        
            if pr.specific_capacitance(content): # checking for specific capacitance values
                all_prop.append(pr.specific_capacitance(content)) # appending the property list
            else:
                all_prop.append(None) # storing None if their is no property mentioned

            if pr.surface_area(content):
                all_prop.append(pr.surface_area(content))
            else:
                all_prop.append(None)

            if pr.energy_density(content):
                all_prop.append(pr.energy_density(content))
            else:
                all_prop.append(None)
                
            if pr.power_density(content):
                all_prop.append(pr.power_density(content))
            else:
                all_prop.append(None)

            if pr.voltage(content):
                all_prop.append(pr.voltage(content))
            else:
                all_prop.append(None)
                
            if pr.current_density(content):
                all_prop.append(pr.current_density(content))
            else:
                all_prop.append(None)

            if pr.cycles(content):
                all_prop.append(pr.cycles(content))
            else:
                all_prop.append(None)
                       
            file.close()  # Close the file before moving

        df.loc[len(df)] = all_prop # adding rows in df for every abstract in loop 
        # print(all_prop)

print(df)
df.to_excel('properties.xlsx', index=False)
   

