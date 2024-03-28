import re

def remove_repeated_characters(text):
    """Remove repeated characters after 'did'"""
    cleaned_text = re.sub(r'(did)\1+', r'\1', text, flags=re.IGNORECASE)
    return cleaned_text
