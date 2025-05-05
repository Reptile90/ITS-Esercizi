'''Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
'''

def show_messages(text_messages):
    for message in text_messages:
        print(message)

text_messages = [
    "Ciao! Come stai?",
    "Oggi c'è il sole.",
    "Ricordati di fare la spesa.",
    "A presto!",
    "Buona serata."
]

show_messages(text_messages)