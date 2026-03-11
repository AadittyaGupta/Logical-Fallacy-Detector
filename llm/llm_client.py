import requests

from config import OLLAMA_URL, MODEL


def call_llm(prompt):
    """
    This function sends a prompt to the Ollama Api and returns the response
    """

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False                     # We'll not stream, we'll get a full response at once
    }

    try:
        # Making POST request to llm Api
        response = requests.post(OLLAMA_URL, json=payload)

        # If the request is successful, return the llm's response text
        if response.status_code == 200:
            return response.json()["response"]
        
        # If the request failed, returning a failure message
        return "LLM request failed"
    
    except Exception as e:
        # Catch exceptions like connection errors and return message
        return f"Error contanting LLM: {e}"