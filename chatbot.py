"""DecodeLabs Project 1 - Rule-Based AI Chatbot"""

BOT_NAME = "Nova"
GREETINGS = {"hi", "hello", "hey", "hola", "good morning", "good afternoon", "good evening"}
EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}


def normalize_input(user_input):
    return " ".join(user_input.lower().strip().split())


def get_response(user_input):
    text = normalize_input(user_input)

    if text in GREETINGS:
        return f"Hello! I'm {BOT_NAME} 🤖. How can I help you today?"
    elif text in EXIT_COMMANDS:
        return f"Goodbye! Thanks for chatting with {BOT_NAME}. Have a great day!"
    elif "how are you" in text:
        return "I'm doing great! Thanks for asking. I'm ready to help."
    elif "your name" in text or text == "who are you":
        return f"My name is {BOT_NAME}. I'm a rule-based AI assistant built with Python."
    elif "what can you do" in text or text == "help":
        return "I can greet you, answer basic questions, explain how I work, and respond to simple AI and Python topics."
    elif "how do you work" in text or "what are your skills" in text:
        return "I use predefined Python rules and decision-making logic to choose my responses."
    elif "thank" in text:
        return "You're welcome! I'm happy to help."
    elif "python" in text:
        return "Python is the language I'm built with for this project. It's excellent for learning programming logic!"
    elif "ai" in text or "artificial intelligence" in text:
        return "AI can involve many approaches. This project demonstrates a simple rule-based approach using explicit programming rules."
    else:
        return "I'm still learning the rules! Try saying 'hello', asking 'what can you do?', or type 'help'."


def run_chatbot():
    print("=" * 55)
    print(f"  {BOT_NAME} - Rule-Based AI Chatbot")
    print("=" * 55)
    print("Type 'help' for available interactions.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print(f"{BOT_NAME}: Please type something so I can respond.")
            continue

        print(f"{BOT_NAME}: {get_response(user_input)}")

        if normalize_input(user_input) in EXIT_COMMANDS:
            break


if __name__ == "__main__":
    run_chatbot()
