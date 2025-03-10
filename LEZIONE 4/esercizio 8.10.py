'''Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.'''



def show_messages(message_list:list[str]):
    send_list:list[str]=[]
    copy_list:list[str]= message_list[:]
    for messaggi in message_list:
        print(messaggi)
        send_list.append(messaggi)
    for copy in copy_list:
        message_list.pop(0)
    print(message_list)
    return send_list


def send_messages(send_list:list[str]):
    print(send_list)


send_messages(show_messages(["Ciao","Come stai?", "Hello", "See you later"]))  
send_messages()  