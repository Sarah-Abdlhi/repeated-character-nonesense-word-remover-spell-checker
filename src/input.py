import pandas as pd
from error_exception import CustomError

def load_csv(dirty_dataset):
    """Load CSV file"""
    try:
        return pd.read_csv(dirty_dataset)
         
    except FileNotFoundError:
        raise CustomError("File not found. Please check the file path.")
