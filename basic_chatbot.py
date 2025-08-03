def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("🤖 Chatbot: Hi!")
        elif user_input in ["how are you", "how are you doing"]:
            print("🤖 Chatbot: I'm fine, thanks! How about you?")
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Chatbot: I'm a simple rule-based chatbot built in Python.")
        elif user_input in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a great day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn’t understand that.")

# Run the chatbot
chatbot()
