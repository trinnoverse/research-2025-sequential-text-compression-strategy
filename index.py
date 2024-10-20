from compressors.lemmatization import lemmatization
from compressors.stemming import stemming
from compressors.stop_word_removal import stop_word_removal
from compressors.synonym_substitution import synonym_substitution
from compressors.normalizer import normalizer
from auxiliars.tokenizer import tokenize
from auxiliars.llm import call_llm

# Input text to be processed
INPUT_TEXT = "I want to know who was the first novel prize of literature."

# Order of compressors to apply
COMPRESSORS = [
    normalizer,
    stop_word_removal,
    # stemming,
    lemmatization,
    synonym_substitution
]

def main():
    """Main function to orchestrate the processing of the input text.
    
    It applies a series of text transformation functions in the order defined in the COMPRESSORS list,
    tokenizes the result, and prints the input, output, tokens, and number of tokens at each step.
    """
    text = INPUT_TEXT
    
    for compressor in COMPRESSORS:
        print(f"Input: {text}")
        text = compressor(text)
        
        # Tokenization
        tokens = tokenize(text)
        
        print(f"Output: {text}")
        print(f"Tokens: {tokens}")
        print(f"Number of tokens: {len(tokens)}")
        
    # Optional: Call to LLM (uncomment to use)
    call_llm(text)
    # print(f"LLM Response: {response}")

if __name__ == "__main__":
    main()
