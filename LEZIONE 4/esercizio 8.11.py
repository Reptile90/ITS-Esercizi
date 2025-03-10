'''Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.'''


def show_messages(message_list:list[str]):
    send_list:list[str]=[]
    copy_list:list[str]= message_list[:]
    for messaggi in message_list:
        print(messaggi)
        send_list.append(messaggi)
    for copy in copy_list:
        message_list.pop(0)
    print(message_list)
    copy_send_list:list[str]= send_list[:]
    return copy_send_list


def send_messages(copy_send_list:list[str]):
    
    print(copy_send_list)

messages:list[str] = ["Ciao","Come stai?", "Hello", "See you later"]
send_messages(show_messages(messages))  
send_messages(show_messages(messages))  