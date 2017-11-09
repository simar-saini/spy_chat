# importing spy and existing friends
from spy_details import Spy, friends
from termcolor import colored

import csv

# function to add new friends.
def add_friend():
    # using class spy
    new_friend = Spy(" ", " ", 0, 0.0)

    # ask user for name and salutation of friend
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation= raw_input("What to call Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = int(raw_input("Age? "))
    new_friend.rating = float(raw_input("Spy rating? "))
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.age < 50 and new_friend.age :


        # add friend if conditions satisfies
        friends.append(new_friend)
        with open('friends.csv', 'wb') as friends_data:
           writer = csv.writer(friends_data)
           writer.writerow([new_friend.name, new_friend.salutation, new_friend.rating, new_friend.age, new_friend.is_online])

        print (colored('Friend Added!', 'magenta'))
    else:
        print (colored('Sorry! Invalid entry. We can\'t add spy with the details you provided\n ', 'blue'))
        print (colored('The convention to follow is: \n ', 'blue'))
        print (colored('1. Name can be alphabets only.\n ', 'blue'))
        print (colored('2. Age can be digits only.\n ', 'blue'))

    # returning total no of friends.
    return len(friends)