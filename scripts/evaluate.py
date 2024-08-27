import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the processed data
input_file = 'data/processed/sp500_features.csv'
data = pd.read_csv(input_file, index_col='Date', parse_dates=True)

# Features and target
X = data[['Close', 'MA50', 'MA200', 'RSI', 'BB_upper', 'BB_lower']]
y = data['Close'].shift(-1)

# Drop the last row with NaN target
X = X[:-1]
y = y[:-1]

# Load the trained model
model_file = 'models/random_forest_model.pkl'
with open(model_file, 'rb') as f:
    model = pickle.load(f)

# Make predictions
predictions = model.predict(X)

# Evaluate the model
mse = mean_squared_error(y, predictions)
print(f"Mean Squared Error: {mse}")

# Plot the results
plt.figure(figsize=(14, 7))
plt.plot(y.index, y, label='Actual Price', color='b')
plt.plot(y.index, predictions, label='Predicted Price', color='r')
plt.title('S&P 500 Actual vs Predicted Prices')
plt.legend()
plt.show()
