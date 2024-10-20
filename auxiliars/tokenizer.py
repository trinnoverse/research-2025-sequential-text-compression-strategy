import os
import tiktoken

MODEL = os.environ.get("LLM_MODEL")

def tokenize(text: str,return_decoded:true):
    """Tokenizes the input text into tokens using the tiktoken library.
    
    Args:
        text (str): The input string to be tokenized.
        return_decoded (bool): Whether the fucntion should return tokend decoded.
        
    Returns:
        list: A list of token IDs generated from the input text.
    """
    encoding = tiktoken.encoding_for_model(MODEL)
    tokens = encoding.encode(text)
    decoded = [encoding.decode([token]) for token in tokens]
    if return_decoded:
        return decoded
    else:
        return tokens

