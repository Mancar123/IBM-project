import matplotlib.pyplot as plt

def plot_data(data, anomalies):
    plt.figure(figsize=(12, 6))
    
    # Plot the sensor values
    plt.plot(data['timestamp'], data['value'], label='Sensor Data', color='blue')
    
    # Highlight anomalies
    plt.scatter(anomalies['timestamp'], anomalies['value'], color='red', label='Anomalies')
    
    plt.title('Sensor Data with Detected Anomalies')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
