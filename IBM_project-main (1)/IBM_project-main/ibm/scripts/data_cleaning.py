import pandas as pd

def clean_data(file_path):
    # Load the dataset
    data = pd.read_csv(r"C:\abhi\ibm\Data\realKnownCause\ambient_temperature_system_failure.csv")
    
    # Ensure 'timestamp' is in datetime format
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    
    # Drop rows with missing values (if any)
    data.dropna(inplace=True)
    
    # Sort by timestamp (if needed)
    data.sort_values(by='timestamp', inplace=True)
    
    return data