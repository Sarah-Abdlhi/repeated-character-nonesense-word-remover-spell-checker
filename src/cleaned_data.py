import pandas as pd

def save_cleaned_data(data, filename):
    """Save cleaned data to a CSV file"""
    try:
        data.to_csv(filename, index=False)
        print("Cleaned data saved successfully.")
    except Exception as e:
        raise CustomError(f"Error saving cleaned data: {e}")
