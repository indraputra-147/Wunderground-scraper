#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 17:27:44 2026

@author: brin
"""

import pandas as pd
import os
import glob
import numpy as np

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    if fahrenheit == '--':
        return 'NaN'
    else:
        celsi = fahrenheit.replace('°F', '')
        celsi = round((float(celsi) - 32) * 5.0/9.0, 3)
        return celsi
    
def safe_humidity_conversion(humidity):
    if humidity == '--' or pd.isna(humidity):
        return 'NaN'  # Return NaN for '--' or missing data
    try:
        return int(humidity[:-2])  # Remove the percentage sign and convert to int
    except Exception:
        return 'NaN'  # Return NaN if there's an error

# Function to convert mph to km/h
def mph_to_kmh(mph):
    if mph == '--':
        return 'NaN'
    else:
        kmh = mph.replace('°mph', '')
        kmh = round(float(kmh) * 1.609344, 3)
    return kmh

# Function to convert inHg to hPa
def inhg_to_hpa(inhg):
    return round(inhg * 33.8639, 3)

# Function to convert inches to mm
def inches_to_mm(inches):
    return round(inches * 25.4, 3)

# Main function to process each CSV file
def process_csv(input_file):
    # Load the CSV file
    df = pd.read_csv(input_file)

    # Clean the column names
    df.columns = df.columns.str.strip()

    # Manually set the correct column names
    df.columns = ['Time', 'Temperature', 'Dew Point', 'Humidity', 'Wind', 'Speed', 'Gust', 'Pressure', 'Precip. Rate.', 'Precip. Accum.', 'UV', 'Solar']

    # Remove the first row (duplicate headers)
    df = df.drop(0)

    # Convert columns with units
    df['Temperature'] = df['Temperature'].apply(fahrenheit_to_celsius)
    df['Dew Point'] = df['Dew Point'].apply(fahrenheit_to_celsius)
    df['Humidity'] = df['Humidity'].apply(safe_humidity_conversion)
    df['Speed'] = df['Speed'].apply(mph_to_kmh)
    df['Gust'] = df['Gust'].apply(mph_to_kmh)

    df['Pressure'] = df['Pressure'].str.replace('°in', '').astype(float).apply(inhg_to_hpa)

    df['Precip. Rate.'] = df['Precip. Rate.'].str.replace('°in', '').astype(float).apply(inches_to_mm)
    df['Precip. Accum.'] = df['Precip. Accum.'].str.replace('°in', '').astype(float).apply(inches_to_mm)
    df['Solar'] = df['Solar'].str[:-4]
    df['Solar'] = np.where(df['Solar'] == '', '0', df['Solar'])
    # Create 'metric' folder if it doesn't exist
    os.makedirs('metric', exist_ok=True)

    # Save the modified DataFre to the new folder in CSV format
    output_path = os.path.join('metric', os.path.basename(input_file))
    df.to_csv(output_path, index=False)

    print(f"Processed file saved as: {output_path}")

# Folder containing the CSV files
folder_path = './'  # Current directory, adjust if needed

# Find all CSV files matching the pattern "IBOGOR*.csv"
csv_files = glob.glob(os.path.join(folder_path, 'IBOGOR*.csv'))

# Process each CSV file found
for file in csv_files:
    process_csv(file)
