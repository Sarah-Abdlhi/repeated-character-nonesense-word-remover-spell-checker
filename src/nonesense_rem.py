from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_nonsense_words(text):
    """Remove nonsense and non-informative words"""
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    cleaned_text = ' '.join(filtered_words)
    return cleaned_text
