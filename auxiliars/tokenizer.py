from dotenv import load_dotenv
import os
import tiktoken
load_dotenv()

MODEL = os.environ.get("MODEL_LLM")

def tokenize(text: str,return_decoded:bool):
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

