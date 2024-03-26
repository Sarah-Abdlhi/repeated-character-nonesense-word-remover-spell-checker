import pandas as pd

def save_cleaned_data(data, filename):
    """Save cleaned data to a CSV file"""
    # Save the cleaned data to a new CSV file
    data.to_csv(filename, index=False)
    print("Cleaned data saved successfully.")

if __name__ == "__main__":
    # Example usage
    cleaned_data = pd.DataFrame({'text': ['Example cleaned text']})
    save_cleaned_data(cleaned_data, "cleaned_data.csv")
