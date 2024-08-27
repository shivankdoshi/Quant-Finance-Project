# S&P 500 Prediction Project

This project predicts the closing price of the S&P 500 index using machine learning techniques.

## Project Structure

- `data/`: Contains raw and processed data.
- `notebooks/`: Jupyter notebooks for data exploration and model development.
- `scripts/`: Python scripts for data collection, feature engineering, model training, and evaluation.
- `models/`: Directory to save trained models.
- `results/`: Contains predictions and plots.
- `config/`: Configuration files.
- `tests/`: Unit tests for the project.

## Setup

1. Clone the repository.
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the scripts in the following order:
    - `data_collection.py`
    - `feature_engineering.py`
    - `model_training.py`
    - `evaluate.py`
    - `predict.py`

## Usage

The model can be used to predict future prices by running the `predict.py` script. The results will be saved in the `results/predictions/` directory.

## License

MIT License
