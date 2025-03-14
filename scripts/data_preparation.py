import pandas as pd

import sys
import os

# Get the parent directory of the project and add to Python path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

def prepare_data(file_path='data/owid-covid-data.csv'):
    # Load data
    data = pd.read_csv(file_path)

    # Filter necessary columns
    data = data[['location', 'date', 'new_deaths', 'population']]

    # Convert date column to datetime format
    data['date'] = pd.to_datetime(data['date'])

    # Aggregate data by continent and month
    data['month'] = data['date'].dt.to_period('M')
    monthly_deaths = data.groupby(['location', 'month'])['new_deaths'].sum().reset_index()

    # Calculate population average for each month
    monthly_population = data.groupby(['location', 'month'])['population'].mean().reset_index()

    # Merge data
    monthly_data = pd.merge(monthly_deaths, monthly_population, on=['location', 'month'])

    # Calculate death rates per 100,000 people
    monthly_data['death_rate'] = (monthly_data['new_deaths'] / monthly_data['population']) * 100000
    
    return monthly_data
