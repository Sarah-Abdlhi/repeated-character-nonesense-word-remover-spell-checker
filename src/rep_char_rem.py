import re

def remove_repeated_characters(text):
    """Remove repeated characters after 'did'"""
    # Implement your logic to remove repeated characters after "did"
    # For example:
    cleaned_text = re.sub(r'(did)\1+', r'\1', text, flags=re.IGNORECASE)
    return cleaned_text

if __name__ == "__main__":
    # Example usage
    text = "He didddddn't want to go."
    cleaned_text = remove_repeated_characters(text)
    print("Cleaned text:", cleaned_text)
