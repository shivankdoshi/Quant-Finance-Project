import pandas as pd
import pickle

# Load the processed data
input_file = 'data/processed/sp500_features.csv'
data = pd.read_csv(input_file, index_col='Date', parse_dates=True)

# Features
X = data[['Close', 'MA50', 'MA200', 'RSI', 'BB_upper', 'BB_lower']]

# Load the trained model
model_file = 'models/random_forest_model.pkl'
with open(model_file, 'rb') as f:
    model = pickle.load(f)

# Make predictions
predictions = model.predict(X)

# Save predictions
output_file = 'results/predictions/sp500_predictions.csv'
data['Predicted_Close'] = predictions
data.to_csv(output_file)

print(f"Predictions saved to {output_file}")
