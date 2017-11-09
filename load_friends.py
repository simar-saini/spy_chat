import csv
from spy_details import Spy
from select_friend import friends
def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            spy = Spy(row[0], row[1], row[2], row[3])
            print spy
            friends.append(spy)
