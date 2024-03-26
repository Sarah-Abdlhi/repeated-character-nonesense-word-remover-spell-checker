from src.input import get_csv_filename, read_csv
from src.rep_char_rem import remove_repeated_characters
from src.nonesense_rem import remove_nonsense_words
from src.spell_checker import correct_spelling
from src.cleaned_data import save_cleaned_data

def main():
    # Step 1: Prompt for CSV filename and load data
    csv_filename = get_csv_filename()
    data = read_csv(csv_filename)
    print("Data loaded successfully.")

    # Step 2: Remove repeated characters
    data['text'] = data['text'].apply(remove_repeated_characters)
    print("Repeated characters removed.")

    # Step 3: Remove nonsense words
    data['text'] = data['text'].apply(remove_nonsense_words)
    print("Nonsense words removed.")

    # Step 4: Correct spelling errors
    data['text'] = data['text'].apply(correct_spelling)
    print("Spelling errors corrected.")

    # Step 5: Save cleaned data
    save_cleaned_data(data, "cleaned_data.csv")

if __name__ == "__main__":
    main()
