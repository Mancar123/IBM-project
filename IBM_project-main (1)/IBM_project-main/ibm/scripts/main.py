from data_cleaning import clean_data
from anomaly_detection import detect_anomalies
from visualization import plot_data

def main():
    # Load and clean the NAB dataset
    cleaned_data = clean_data("Data/realKnownCause/ambient_temperature_system_failure.csv")
    
    # Detect anomalies
    anomalies = detect_anomalies(cleaned_data)
    
    # Visualize the data and anomalies
    plot_data(cleaned_data, anomalies)
    
    # Save cleaned data and anomalies
    cleaned_data.to_csv("outputs/cleaned_data.csv", index=False)
    anomalies.to_csv("outputs/anomalies.csv", index=False)

if __name__ == "__main__":
    main()
