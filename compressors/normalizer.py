import re

def normalizer(text: str) -> str:
    """Normalizes the input text by removing non-alphanumeric characters and converting to lowercase.
    
    Args:
        text (str): The input string to be normalized.
        
    Returns:
        str: The normalized version of the input text.
    """
    # Replace non-alphanumeric characters with space
    text = re.sub(r'\W+', ' ', text)  
    return text.lower().strip()
