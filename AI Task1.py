import re

def chatbot_response(user_input):
    # Define patterns for different types of user inputs
    greetings = r"(hi|hello|hey|good (morning|afternoon|evening))"
    how_are_you = r"(how are you|how are you doing)"
    age_question = r"what is your age"
    joke_request = r"tell me a joke"
    goodbye = r"(bye|goodbye|see you later)"

    # Match user input to patterns
    if re.search(greetings, user_input, re.IGNORECASE):
        return "Hello Deeksh! How can I assist you today?"
    elif re.search(how_are_you, user_input, re.IGNORECASE):
        return "I'm just a bot, but thanks for asking!"
    elif re.search(age_question, user_input, re.IGNORECASE):
        return "I'm just a program, so I don't have an age!"
    elif re.search(joke_request, user_input, re.IGNORECASE):
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif re.search(goodbye, user_input, re.IGNORECASE):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Welcome to the advanced chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))
            break
        else:
            print("Bot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
