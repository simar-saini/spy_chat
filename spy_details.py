# importing datetime to show time and date of chat.
from datetime import datetime

# class for spy
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('SIMRAN', 'Mrs.', 19, 4.7)

friend_one = Spy('Mansi, ', 'Mrs.', 21, 4.8)
friend_two = Spy('Karan, ', 'Mr.', 20, 4.6)
friends = [friend_one, friend_two]