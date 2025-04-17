responses = {
    "Hi": "Hello! How can I help you?",
    "Hello": "Hi there how can I help?",
    "What do you serve?":"We have coffee and tea",
    "Do you accept credit cards?":"We accept most major credit cards, and paypal",
    "Alright got it! Thank you!":"Happy to help!"
}

print("Let's chat! type 'quit' to exit")

while True:
    user_input = input("You: ")
    found = False
    
    for key in responses:
        if key in user_input:
            print("Chatbot:", responses[key])
            found = True
            break
            
    if not found:
        print("Chatbot: I'm not sure how to respond to that.")
    
    if "quit" in user_input:
        break
