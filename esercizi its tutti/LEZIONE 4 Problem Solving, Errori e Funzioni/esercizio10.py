''' Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.'''

def send_messages(messages, sent_messages):
    print("Sending messages:")
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

all_messages = ["Hello!", "How are you?", "What's up?", "Goodbye!"]
sent_messages = []

send_messages(all_messages[:], sent_messages)

print("\nOriginal list of messages:")
print(all_messages)
print("\nList of sent messages:")
print(sent_messages)