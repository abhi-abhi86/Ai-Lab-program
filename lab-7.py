def simple_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hello! How can I help you?")
            
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm ready to assist you!")
            
        elif "name" in user_input:
            print("Chatbot: I am a simple Python Chatbot.")
            
        elif "bye" in user_input or "goodbye" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break
            
        else:
            print("Chatbot: I don't understand that. Can you rephrase?")

if __name__ == "__main__":
    simple_chatbot()