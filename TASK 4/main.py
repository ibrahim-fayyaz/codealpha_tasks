print("---- Welcome to a chatbot ----")

def start_chatbot():
    while True:
        user_input = input("Enter a sentence: ")
        print(generate_response(user_input))
        if generate_response(user_input) in "bye" or user_input in "bye":
            break

def generate_response(user_input):
    if user_input in ["hello" , "hi" , "hey"]:
        return "hi there!"
    elif user_input in ["how are you?" , "how are you doing?" , "how are you do"]:
        return "I'm fine!"
    elif user_input in ["I'm fine!" , "I'm good"]:
        return "Im fine too!"
    elif user_input in ["bye" , "bye" , "goodbye"]:
        return "bye"
    return user_input

start_chatbot()