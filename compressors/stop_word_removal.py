import nltk
from nltk.corpus import stopwords

# Download NLTK resources if necessary
nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))

def stop_word_removal(text: str) -> str:
    """Removes stop words from the input text.
    
    Args:
        text (str): The input string containing words from which stop words will be removed.
        
    Returns:
        str: The input text without stop words.
    """
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)
