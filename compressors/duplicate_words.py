def duplicate_words_removal(text: str) -> str:
    """Removes duplicate words from the input text while retaining the first occurrence.

    Args:
        text (str): The input string from which duplicate words will be removed.

    Returns:
        str: The text after removing duplicate words.
    """
    # Split the text into words
    words = text.split()
    
    # Create a set to track seen words and a list for the result
    seen = set()
    result = []

    for word in words:
        # Check if the word has already been seen
        if word.lower() not in seen:  # Case-insensitive check
            seen.add(word.lower())  # Add to the seen set
            result.append(word)  # Retain the first occurrence

    # Join the result list back into a string
    return ' '.join(result)
