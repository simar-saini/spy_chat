# importing older friend if exist
from spy_details import friends,Spy
from termcolor import colored
import csv

def select_friend():


    counter = 1
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            print row

    for friend in friends:
        print str(counter) + ". " + friend.name + "Age : " + str(friend.age)

        counter = counter + 1

    result = int(raw_input(colored("\nSelect from the list : ", 'magenta')))
    return result - 1