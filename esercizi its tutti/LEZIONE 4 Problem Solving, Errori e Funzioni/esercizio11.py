'''Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.'''


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