import os
from openai import OpenAI

# Configuration for the OpenAI API (set your API key and model here)
API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("LLM_MODEL")


client = OpenAI(
    api_key=API_KEY
)


def call_llm(text: str):
    """Calls the OpenAI API to generate a response based on the input text.
    
    Args:
        text (str): The input string that will be sent to the OpenAI model.
        
    Returns:
        str: The response generated by the OpenAI model.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model=MODEL
    )
    response_message = chat_completion.choices[0].message.content
    return response_message


