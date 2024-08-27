import pandas as pd
import os

# Load the raw data
input_file = 'data/raw/sp500.csv'
output_file = 'data/processed/sp500_features.csv'

data = pd.read_csv(input_file, index_col='Date', parse_dates=True)

# Create Moving Averages
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

# Create RSI
delta = data['Close'].diff(1)
gain = delta.where(delta > 0, 0.0)
loss = -delta.where(delta < 0, 0.0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
data['RSI'] = 100 - (100 / (1 + rs))

# Create Bollinger Bands
data['BB_upper'] = data['MA50'] + 2 * data['Close'].rolling(window=50).std()
data['BB_lower'] = data['MA50'] - 2 * data['Close'].rolling(window=50).std()

# Drop rows with missing values
data.dropna(inplace=True)

# Save processed data
os.makedirs(os.path.dirname(output_file), exist_ok=True)
data.to_csv(output_file)

print(f"Feature engineering complete. Data saved to {output_file}")
