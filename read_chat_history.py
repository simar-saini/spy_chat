# importing select friend and spy details (friend details here from spy details)
from select_friend import select_friend
from spy_details import friends
from termcolor import colored

# function to read chat history
def read_chat_history():
    read_chat = select_friend()

    print '\n'

    for chat in friends[read_chat].chats:
      if chat.sent_by_me:
         print '[%s] %s: %s' % (colored(chat.time.strftime("%d %B %Y"), 'blue'), 'You said:', chat.message)
      else:
       print '[%s] %s said: %s' %(colored(chat.time.strftime("%d %B %Y"), 'blue'), colored(friends[read_chat].name, 'red'), chat.message)

