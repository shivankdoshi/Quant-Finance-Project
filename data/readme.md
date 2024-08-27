# Data Directory

This directory contains all the data used in the S&P 500 prediction project.

## Structure

- **`raw/`**: Contains raw, unprocessed data files. These files are typically downloaded directly from external sources such as Yahoo Finance or other data providers.
  
- **`processed/`**: Contains cleaned and processed data files. These files have been transformed through various data processing steps (e.g., feature engineering) and are ready to be used for modeling.
  
- **`external/`**: Contains external datasets that may supplement the primary dataset. These could include macroeconomic indicators, sentiment analysis data, or any other relevant data sources.

## Notes

- Always keep the raw data unmodified. Any transformations should be saved in the `processed/` directory.
- Use appropriate naming conventions for files to make it easy to track the data’s evolution.
