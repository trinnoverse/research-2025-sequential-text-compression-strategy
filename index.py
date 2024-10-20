from dotenv import load_dotenv
import os

from compressors.lemmatization import lemmatization
from compressors.stemming import stemming
from compressors.stop_word_removal import stop_word_removal
from compressors.synonym_replacement import synonym_replacement
from compressors.normalizer import normalizer
from compressors.frequent_words import frequent_words_replacement
from compressors.duplicate_words import duplicate_words_removal
from compressors.abbreviations import text_abbreviation
from auxiliars.tokenizer import tokenize
from auxiliars.llm import call_llm

load_dotenv()


# Input text to be processed
INPUT_TEXT = "Hello, good morning. I'm writing because I want to schedule an appointment with the doctor next week."

# Order of compressors to apply
COMPRESSORS = [
    # text_abbreviation,
    # normalizer,
    # stop_word_removal,
    # synonym_replacement,
    # frequent_words_replacement,
    # # stemming,
    # lemmatization,
    # duplicate_words_removal,
]

# Output file
output_file = f"output_{os.environ.get('MODEL_LLM')}_complemento.txt"

#  hi writing want agenda appointment doctor next week
# hi writing want agenda appt dr next week
def main():
    """Main function to orchestrate the processing of the input text.
    
    It applies a series of text transformation functions in the order defined in the COMPRESSORS list,
    tokenizes the result, and prints the input, output, tokens, and number of tokens at each step.
    """
    with open(output_file, "w") as f:

        text = INPUT_TEXT
        
        for compressor in COMPRESSORS:
            f.write(f"Input: {text}\n")
            f.write(f"Compressor: {compressor.__name__}\n")
            
            text = compressor(text)
            
            # Tokenization
            tokens = tokenize(text,True)
            
            f.write(f"Output: {text}\n")
            f.write(f"Tokens: {'   #'.join(tokens)}\n")
            f.write(f"Number of tokens: {len(tokens)}\n")

            # Optional: Call to LLM (uncomment to use)
            llm_response=call_llm(text)
            f.write(f"LLM Multidimensional evaluation: \n{llm_response}\n")

            f.write(f"\n\n")
if __name__ == "__main__":
    main()
