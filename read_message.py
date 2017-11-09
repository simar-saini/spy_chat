# importing friend, steganography library, and datetime
from select_friend import select_friend
from steganography.steganography import Steganography
from spy_details import friends
from spy_details import ChatMessage
from termcolor import colored
from colorama import init
import csv
init()

# function for read message
def read_message():
    # choose friend from the list to communicate
    sender = select_friend()
    with open('chats.csv', 'rb') as chat_data:
        reader = csv.reader(chat_data)
        for row in reader:
            print row

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)
    print "The secret message is ",
    print (colored(secret_message, 'red'))
    new = (secret_message.upper()).split()
    with open('chats.csv', 'wb') as chatdata:
        writer = csv.writer(chatdata)
        writer.writerow([secret_message])
    if "SOS" in new or "SAVE" in new or "HELP" in new or "ACCIDENT" in new or "ALERT" in new:
       print (colored("!", 'grey', 'on_yellow')),
       print (colored("!", 'grey', 'on_yellow')),
       print (colored("!", 'grey', 'on_yellow'))
       print (colored("The friend who sent this message need your help.", 'cyan'))
       print (colored("You can help your friend by sending helping message.", 'cyan'))
       print (colored("Select the friend to send helping message", 'red'))
       print (colored("You just sent a message to help your friend.", 'magenta'))
       new_chat = ChatMessage(secret_message, False)
       friends[sender].chats.append(new_chat)
       print (colored("Your secret message has been saved.", 'cyan'))


    else:
        print(colored("This image has no secret message. No decoding"))

