def frequent_words_replacement(text: str) -> str:
    """Replaces common words and phrases in the input text with specified alternatives.

    Args:
        text (str): The input string in which words and phrases will be replaced.

    Returns:
        str: The text after replacing specified words and phrases.
    """
    # Define a dictionary for word replacements
    replacements = {
        "hello": "hi",
        "good morning": "hi",
        "goodbye": "bye",
        "thank you": "thanks",
        "please": "plz",
        "you're welcome": "yw",
        "how are you?": "howdy",
    }

    # Iterate over the replacements and substitute in the text
    for target, replacement in replacements.items():
        text = text.replace(target, replacement)

    return text
