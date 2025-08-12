#task 4 is my simple chatbot
def get_response(user_input):
    # hum idhr aur bhi add kr sakty hein
    if user_input == "hello" or user_input == "hi":
        return "Hi there!"
    elif user_input == "how are you":
        return "I'm fine, thanks for asking!"
    elif user_input == "what is your name":
        return "i am a python chatbot made by a student"
    elif user_input == "what is your age":
        return "maximum life until computer exist"
    elif user_input == "who made you":
        return "a student here in rawalpindi/islamabad"
    elif user_input == "where do you live":
        return "in memory of computer hehe"
    elif user_input == "what is the time":
        import datetime
        now = datetime.datetime.now()
        return f"ajj ka waqt hy {now.strftime('%H:%M:%S')}"
    elif user_input == "what is the date":
        import datetime
        today = datetime.date.today()
        return f"today its {today.strftime('%d %B %Y')}"
    elif user_input == "tell me a joke":
        return "i m not your joker. huh"
    elif user_input == "bye":
        return "ALLAH HAFIZ"
    else:
        return "Maazrat, main yeh nahi samjh sakta boss"

def chatbot():
    print("Chatbot: Hey, i m your simple chatbot ask me anything")
    message_count = 0  # to count how many messages user sent

    while True:
        user_input = input("You: ").lower().strip()
        message_count += 1

        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input == "bye":
            print(f"Chatbot: You sent me {message_count} messages today. Bye!")
            break

#we start chatbot which will start the loop of bot
chatbot()
