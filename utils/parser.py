
def parse_response(response_text):
    """
    Parses the LLM's raw text response into a structured dictionary , handling multi-line outputs and Markdown formatting safely.
    """
    result = {
        "fallacy": "",
        "explanation": "",
        "suggestion": "",
        "reasoning": ""
    }

    # Handle potential connection errors from llm_client.py
    if "LLM request failed" in response_text or "Error contanting LLM" in response_text:
        result["fallacy"] = "Connection Error"
        result["explanation"] = response_text
        return result

    current_key = None
    lines = response_text.split("\n")

    for line in lines:
        # Create a clean version of the line just for checking headers
        # This removes bolding (**) so our .startswith() check works safely
        clean_line = line.lower().replace("**", "").strip()
        
        if clean_line.startswith("fallacy type"):
            current_key = "fallacy"
            content = line.split(":", 1)[-1].replace("**", "").strip()
            if content: result[current_key] += content + "\n"
                
        elif clean_line.startswith("explanation"):
            current_key = "explanation"
            content = line.split(":", 1)[-1].replace("**", "").strip()
            if content: result[current_key] += content + "\n"
                
        elif clean_line.startswith("suggested improvement"):
            current_key = "suggestion"
            content = line.split(":", 1)[-1].replace("**", "").strip()
            if content: result[current_key] += content + "\n"
                
        elif clean_line.startswith("reasoning"):
            current_key = "reasoning"
            content = line.split(":", 1)[-1].replace("**", "").strip()
            if content: result[current_key] += content + "\n"
                
        else:
            # If it's not a header, append it to the current active section.
            # We'll use \n so bullet points in the LLM response render correctly in Streamlit.
            if current_key and line.strip():
                result[current_key] += line.strip() + "\n"

    # Cleans up trailing whitespace and newlines
    for key in result:
        result[key] = result[key].strip()

    return result