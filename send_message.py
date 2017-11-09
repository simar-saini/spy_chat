# importing existing friend, steganography library, and datetime.
from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import friends, ChatMessage
from termcolor import colored

# function to send a secret message.
def send_message():


    friend_choice = select_friend()
    original_image = raw_input("Provide the name of the image to hide the message : ")
    output_image = raw_input("Provide the name of the output image  : ")
    text = raw_input("Enter your message here : ")
    Steganography.encode(original_image, output_image, text)
    new_chat = ChatMessage(text, True)
    friends[friend_choice].chats.append(new_chat)
    print (colored("Your message encrypted successfully.", 'red'))
    new_chat = {
        'message': text,
        'time': datetime.now(),
        'sent_by_me': True
    }
    friends[friend_choice].chats.append(new_chat)
    print (colored("your secret message is ready.",'yellow'))
