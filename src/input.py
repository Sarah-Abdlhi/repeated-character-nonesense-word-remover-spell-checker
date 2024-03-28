#import pandas as pd
import csv
from error_exception import CustomError

def load_csv(dirty_dataset):
    """Load CSV file"""
    try:
        with open(dirty_dataset, 'r', newline='', encoding='utf-8') as csvfile:
            data = [row[0] for row in csv.reader(csvfile)]
        return data
    except FileNotFoundError:
        raise CustomError("File not found. Please check the file path.")
