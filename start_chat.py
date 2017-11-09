# import statements
from globals import current_status_message
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
from read_chat_history import read_chat_history
from termcolor import colored

# start_chat() function definition.
def start_chat(name, age, rating, status):
    from globals import current_status_message
    if not (age > 12 and age < 50) :
        error_message = "Invalid age. Provide correct details."
        print (colored(error_message,"red"))
    else:
        welcome_message = "Authentication complete. Welcome\n\n" \
                          "Name : " + name + "\n" \
                          "Age: " + str(age) + "\n" \
                          "Rating: " + str(rating) + "\n" \
                          "Proud to have you on board\n"
        print welcome_message
        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n\n " \
                           "1. Add a status update \n " \
                           "2. Add a friend \n " \
                           "3. Send a secret message \n " \
                           "4. Read a secret message \n " \
                           "5. Read Chats from a user \n " \
                           "6. Close Application \n\n"
            result = int(raw_input(menu_choices))
            if (result == 1):
                current_status_message = add_status(current_status_message)
            elif (result == 2):
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif(result == 3):
                send_message()
            elif (result == 4):
                read_message()
            elif(result == 5):
                read_chat_history()
            elif (result == 6):
                show_menu = False
            else:
                print (colored("wrong choice try again.", 'green'))
                exit()