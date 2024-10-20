import os
import tiktoken

MODEL = os.environ.get("LLM_MODEL")

def tokenize(text: str):
    """Tokenizes the input text into tokens using the tiktoken library.
    
    Args:
        text (str): The input string to be tokenized.
        
    Returns:
        list: A list of token IDs generated from the input text.
    """
    encoding = tiktoken.get_encoding(MODEL)
    tokens = encoding.encode(text)
    return tokens
