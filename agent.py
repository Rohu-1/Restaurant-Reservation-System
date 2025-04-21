from llm import call_llm

def handle_input(user_input: str, session_state) -> str:
    """
    Handles the user input, classifies intent, and returns a response.
    """
    intent = classify_intent(user_input)
    return intent

def classify_intent(user_input: str) -> str:
    """
    Uses LLM to classify the intent of the user input.
    """
    prompt = f"Classify the following user input and provide the intent:\n{user_input}"
    response = call_llm(prompt)
    return response.strip().lower()
