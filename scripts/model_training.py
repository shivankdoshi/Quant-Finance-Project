import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle
import os

# Load the processed data
input_file = 'data/processed/sp500_features.csv'
data = pd.read_csv(input_file, index_col='Date', parse_dates=True)

# Features and target
X = data[['Close', 'MA50', 'MA200', 'RSI', 'BB_upper', 'BB_lower']]
y = data['Close'].shift(-1)  # Predict next day's closing price

# Drop the last row with NaN target
X = X[:-1]
y = y[:-1]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# Save the model
model_dir = 'models/'
os.makedirs(model_dir, exist_ok=True)
model_file = os.path.join(model_dir, 'random_forest_model.pkl')
with open(model_file, 'wb') as f:
    pickle.dump(model, f)

print(f"Model training complete. Model saved to {model_file}")
