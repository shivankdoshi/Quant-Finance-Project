import yfinance as yf
import os

# Define the output path for the data
output_dir = 'data/raw/'
os.makedirs(output_dir, exist_ok=True)

# Download historical data for S&P 500
data = yf.download('^GSPC', start='2010-01-01', end='2024-01-01')

# Save to CSV
data.to_csv(os.path.join(output_dir, 'sp500.csv'))

print("Data collection complete. Data saved to data/raw/sp500.csv")
