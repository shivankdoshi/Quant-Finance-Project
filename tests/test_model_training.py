import unittest
import os
import pickle

class TestModelTraining(unittest.TestCase):
    def test_model_training(self):
        model_file = 'models/random_forest_model.pkl'
        self.assertTrue(os.path.exists(model_file), "Model file should exist after training.")

        with open(model_file, 'rb') as f:
            model = pickle.load(f)
            self.assertIsNotNone(model, "Loaded model should not be None.")

if __name__ == '__main__':
    unittest.main()
