import unittest
import pandas as pd
import os

class TestDataProcessing(unittest.TestCase):
    def test_data_loading(self):
        input_file = 'data/raw/sp500.csv'
        data = pd.read_csv(input_file)
        self.assertTrue(not data.empty, "Raw data should not be empty.")

    def test_feature_engineering(self):
        input_file = 'data/processed/sp500_features.csv'
        data = pd.read_csv(input_file)
        self.assertTrue('MA50' in data.columns, "MA50 feature should be present.")
        self.assertTrue('RSI' in data.columns, "RSI feature should be present.")

if __name__ == '__main__':
    unittest.main()
