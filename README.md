
# Text Compression Techniques for NLP

This repository contains the implementation of various text compression techniques used in **NLP** preprocessing, directly tied to the research presented in our paper. The code is designed to process and transform text by applying multiple techniques in a sequential manner, as described in the article. It focuses on improving efficiency by reducing the number of tokens, stemming, lemmatizing, and normalizing input data.

The details of the underlying techniques and the reasoning behind them are discussed in the paper. To gain a deeper understanding, please refer to the full article.

## General Overview of the Article

The paper introduces a set of text preprocessing techniques aimed at optimizing inputs for large language models (LLMs). These techniques include stop-word removal, synonym substitution, stemming, lemmatization, and contraction. The code in this repository reflects these concepts and provides an implementation of these techniques, showing how they can be applied to real-world text processing tasks.

## Project Structure

The project is organized as follows:

```
.
├── assets/
│   ├── diagram.drawio             # Diagrams for the paper.
├── compressors/
│   ├── abbreviations.py           # Contracts words into abbreviations.
│   ├── duplicate_words.py         # Removes consecutive repeated words in the text.
│   ├── frequent_words.py          # Replaces predefined frequent words or phrases.
│   ├── lemmatization.py           # Applies lemmatization to reduce words to their base form.
│   ├── normalizer.py              # Normalizes text (e.g., lowercasing, punctuation removal).
│   ├── stemming.py                # Applies stemming to reduce words to their root form.
│   ├── stop_word_removal.py       # Removes common stop words from the text.
│   ├── synonym_replacement.py    # Replaces words with synonyms, if the synonym is shorter.
├── auxiliars/
│   ├── downloads.py               # Aditional downloads (corpus, dictionaries, etc,) for nltk library.
│   ├── tokenizer.py               # Tokenizes and decodes text using the tiktoken library.
│   ├── llm.py                     # Uses OpenAI's API to generate responses (model and API key are parametrized).
├── results/
│   ├── **.txt                     # Path where the results are set.
├── index.py                       # Orchestrator: applies each compression technique sequentially.
├── requirements.txt               # Python dependencies for the project.
├── .env                           # Environment variables for OpenAI API key and model (not included in repository).
└── README.md                      # Project documentation.
```

## Installation & Setup

To run this project, follow the steps below:

### 1. Set Up a Virtual Environment

First, create and activate a Python virtual environment:

```bash
# Linux/Mac
python -m venv virtual-env
source virtual-env/bin/activate

# Windows
python -m venv virtual-env
virtual-env\Scripts\activate
```

### 2. Install Dependencies

Once the virtual environment is active, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Ensure you have an `.env` file in the root directory to store your environment variables, including your OpenAI API key and model. Example:

```
OPENAI_API_KEY=your-openai-api-key
MODEL_LLM=gpt-3.5-turbo
```

### 4. Run the Code

To execute the code, simply run `index.py`. The text processing will be performed using the sequential order of the techniques defined in the script. The input text, output text, and tokenization details will be printed in the terminal and saved to an `output.txt` file.

```bash
python index.py
```

The file `output.txt` will contain:

- The original and transformed text after each compression step.
- A list of tokens and their count.
- Changes made by each compressor (e.g., original word -> replaced word).

## Additional Notes

- The compressors apply transformations such as stop-word removal, synonym substitution (only if the synonym is shorter), and abbreviation contraction. Each compressor outputs both the transformed text and a log of changes made.
- To explore more about the theory and benefits of these techniques, please read our paper linked in this repository.

## Paper

For more information on the methods used and the theoretical background, please refer to our [paper here](#).
