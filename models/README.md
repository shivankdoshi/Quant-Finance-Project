# Models Directory

This directory contains the machine learning models used in the S&P 500 prediction project.

## Contents

- **`random_forest_model.pkl`**: This is the serialized Random Forest model trained on the processed data. The model can be loaded and used to make predictions on new data.
  
- **`scaler.pkl`**: This file contains the scaler used to normalize or standardize the features before training the model. It is important to apply the same scaling to any new data before making predictions with the trained model.

## Notes

- Ensure that you save the models with appropriate versioning if you train multiple models or experiment with different hyperparameters.
- Keep track of which features and preprocessing steps were used when training each model.
