from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    # Initialize Isolation Forest
    model = IsolationForest(contamination=0.05, random_state=42)
    
    # Fit model on 'value' column
    data['anomaly'] = model.fit_predict(data[['value']])
    
    # Filter anomalies
    anomalies = data[data['anomaly'] == -1]
    return anomalies
