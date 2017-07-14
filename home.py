import sys
from io import StringIO
zen = StringIO()
old_stdout = sys.stdout
sys.stdout = zen
import this
sys.stdout = old_stdout
book = zen.getvalue()
#set up necessary variables
game = True
room = 1

while game: #the condition that keeps the game running

  # TODO: if/elif/else statements, each should be a separate room
  if room == 1:
      #TODO: print a description about the room and what’s in it
      print('You are in room 1, you see your mum.')
      print('Let\'s type "hello" to greet her or "leave" to leave the room.')
      #offer some options to player
      #take in their input
      usr_input = input('hello or leave? ')
      #use more if/elif/else statements to move from room to room based on user input
      if usr_input == 'hello':
           #TODO: have user do something. One of the conditions should set room = 2 to move to the next room
           print('Hello mum!')
      elif usr_input == 'leave':
          room =2
          print('You left room 1 for room 2')
      else:
          print('Invalid input, please try again!')
  elif room == 2:
        print('You are in room 2, you found a book called "Zen of Python".')
        print('Type "read" to read it or "room1" to go to room 1 or "room3" to go to room 3')
        usr_input = input('read or room1 or room3? ')
        if usr_input == 'read':
            print(book)
        elif usr_input == 'room1':
            room = 1
            print('You left room 2 for room 1')
        elif usr_input == 'room3':
            room = 3
            print('You left room 2 for room 3')
        else:
            print('Invalid input, please try again!')
  else:
        print('You are in room 3, you see a door, but it is locked.')
        print('Type "pick" to pick the lock and leave the house or "room2" to back to room 2')
        usr_input = input('pick or room2? ')
        if usr_input == 'pick':
            print('You attempt to pick the lock...')
            print('You picked the lock and leave the house, game ended!')
            game = False
        elif usr_input == 'room2':
            room = 2
            print('You left room 3 for room 2')
        else:
            print('Invalid input, please try again!')


#One or more of your rooms must have code that allows you to exit the while loop:
#game = false
