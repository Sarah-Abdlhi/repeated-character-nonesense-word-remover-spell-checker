from spellchecker import SpellChecker

# Create an instance of SpellChecker
spell_checker = SpellChecker()

# Add custom dictionary of correct spellings
custom_dictionary = {
    'ogle': 'google',  # Add correct spelling for 'ogle'
    'nonmember': 'November'
}

# Update the spell checker with the custom dictionary
spell_checker.word_frequency.load_words(custom_dictionary.keys())

def correct_spelling(text):
    """Correct spelling errors"""
    # Tokenize the text into words
    words = text.split()

    # Correct spelling for each word
    corrected_words = []
    for word in words:
        # Get the corrected version of the word
        corrected_word = spell_checker.correction(word)
        if corrected_word is not None:
            # Check if the corrected word is in the custom dictionary
            corrected_word = custom_dictionary.get(corrected_word, corrected_word)
            corrected_words.append(corrected_word)
        else:
            # If the corrected word is None, use the original word
            corrected_words.append(word)

    # Join the corrected words back into a single string
    corrected_text = ' '.join(corrected_words)
    return corrected_text
