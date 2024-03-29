import re
from nltk.corpus import stopwords

def remove_nonsense_words(text):
    """Remove nonsense and non-informative words"""
    # Custom list of non-informative words
    non_informative_words = set(['jkhhnb'])  # non-informative words added
    
    stop_words = set(stopwords.words('english'))

    # Define a regular expression pattern to match words
    word_pattern = re.compile(r'\b\w+\b', flags=re.IGNORECASE)

    # Find all words in the text
    words = word_pattern.findall(text)

    # Filter out non-informative words and NLTK's stopwords
    filtered_words = [word for word in words if len(word) > 1 and word.lower() not in stop_words and word.lower() not in non_informative_words]

    # Join the remaining words into a cleaned text string
    cleaned_text = ' '.join(filtered_words)
    return cleaned_text
