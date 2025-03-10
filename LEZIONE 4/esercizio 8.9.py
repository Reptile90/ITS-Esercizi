'''Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message'''


def show_messages(messagelist:list[str]):
    for messaggi in messagelist:
        print(messaggi)



show_messages(["Ciao", "Salve", "Arrivederci","Hello", "See you later"])