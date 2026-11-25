def get_bot_response(user_input: str) -> str:
    """Return a predefined reply based on user input."""
    cleaned_input = user_input.strip().lower()

    if cleaned_input in ("hello", "hi", "hey"):
        return "Hi!"
    elif cleaned_input in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif cleaned_input in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."


def run_chatbot() -> None:
    """Run the interactive rule-based chatbot loop."""
    print("Chatbot started! Type 'bye' to exit.")

    while True:
        user_message = input("You: ")
        reply = get_bot_response(user_message)
        print(f"Bot: {reply}")

        if user_message.strip().lower() in ("bye", "goodbye", "exit"):
            break


if __name__ == "__main__":
    run_chatbot()