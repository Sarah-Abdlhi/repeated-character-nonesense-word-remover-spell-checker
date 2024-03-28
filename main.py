import nltk
nltk.download('stopwords')
nltk.download('punkt')  # download the 'punkt' tokenizer

from src.error_exception import CustomError, load_csv
from src.rep_char_rem import remove_repeated_characters
from src.nonesense_rem import remove_nonsense_words
from src.spell_checker import correct_spelling
from src.cleaned_data import save_cleaned_data

def main():
    try:
        # Step 1: Load CSV file
        data = load_csv('dirty_dataset.csv')
        print("Data loaded successfully.")

        # Check if the DataFrame is empty
        if data.empty:
            raise CustomError("The CSV file is empty.")

        # Step 2: Remove repeated characters
        data['text'] = data.apply(lambda row: remove_repeated_characters(row[0]), axis=1)
        print("Repeated characters removed.")

        # Step 3: Remove nonsense words
        data['text'] = data['text'].apply(remove_nonsense_words)
        print("Nonsense words removed.")

        # Step 4: Correct spelling errors
        data['text'] = data['text'].apply(correct_spelling)
        print("Spelling errors corrected.")

        # Step 5: Save cleaned data
        save_cleaned_data(data, "cleaned_data.csv")

    except CustomError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
