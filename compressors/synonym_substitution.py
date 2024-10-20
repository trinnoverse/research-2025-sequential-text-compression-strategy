from nltk.corpus import wordnet

def synonym_substitution(text: str) -> str:
    """Substitutes words in the input text with their synonyms.
    
    Args:
        text (str): The input string containing words to be substituted.
        
    Returns:
        str: The input text with words substituted by their synonyms.
    """
    words = text.split()
    substituted_words = []
    
    for word in words:
        synonyms = wordnet.synsets(word)
        if synonyms:
            substituted_words.append(synonyms[0].lemmas()[0].name())  # Substitute with the first synonym
        else:
            substituted_words.append(word)

    return ' '.join(substituted_words)
