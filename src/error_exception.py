import pandas as pd

class CustomError(Exception):
    """Custom exception class for handling errors"""
    pass

def load_csv(filename):
    """Load CSV file"""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        raise CustomError("File not found. Please check the file path.")
