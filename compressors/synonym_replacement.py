import nltk
from nltk.corpus import wordnet

# Ensure that the WordNet corpus is downloaded
nltk.download('wordnet')

def synonym_replacement(text: str) -> str:
    """Substitutes words in the input text with their synonyms if the synonym is shorter than the original word.

    Args:
        text (str): The input string in which synonyms will be substituted.

    Returns:
        str: The text after substituting words with shorter synonyms where applicable.
    """
    words = text.split()
    new_words = []

    for word in words:
        # Find synonyms for the current word
        synonyms = wordnet.synsets(word)

        # If synonyms are found, choose the first one
        if synonyms:
            # Get the first synonym's lemma
            synonym = synonyms[0].lemmas()[0].name()
            # Check if the synonym is shorter than the original word
            if len(synonym) < len(word):
                new_words.append(synonym.replace('_', ' '))  # Replace underscores with spaces
            else:
                new_words.append(word)
        else:
            new_words.append(word)

    return ' '.join(new_words)
