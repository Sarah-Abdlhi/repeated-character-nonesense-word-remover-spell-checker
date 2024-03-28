import csv
import nltk
from nltk.tokenize import word_tokenize
import re

# Download NLTK resources
nltk.download('punkt')

# Function to remove repeated characters from a word
def remove_repeated_characters(word):
    return re.sub(r'(.)\1+', r'\1', word)

# Function to process a single row of data
def process_row(row):
    # Tokenize the text into words
    words = word_tokenize(row)
    
    # Remove repeated characters from each word
    cleaned_words = [remove_repeated_characters(word) for word in words]
    
    # Join the cleaned words back into a single string
    cleaned_text = ' '.join(cleaned_words)
    
    return cleaned_text

# Function to process the CSV file
def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        
        # Process each row and write cleaned data to new CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
            writer = csv.writer(output_csv)
            for row in reader:
                cleaned_text = process_row(row[0])  # Assuming the text is in the first column
                writer.writerow([cleaned_text])
