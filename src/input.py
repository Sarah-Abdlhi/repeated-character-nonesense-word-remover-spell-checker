import pandas as pd
from error_exception import CustomError

def get_csv_filename():
    """Prompt the user to enter the CSV filename"""
    filename = input("Enter the CSV filename: ")
    if not filename.endswith('.csv'):
        raise CustomError("Invalid file format. Please provide a CSV file.")
    return filename

def read_csv(filename):
    """Read CSV file"""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        raise CustomError("File not found. Please check the file path.")

if __name__ == "__main__":
    try:
        csv_filename = get_csv_filename()
        data = read_csv(csv_filename)
        print("Data loaded successfully.")
    except CustomError as e:
        print("Error:", e)
