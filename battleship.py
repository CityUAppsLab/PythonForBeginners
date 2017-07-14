# import the random functions library
from random import randint

# empty board list
board = []

# the next few lines generate an empty board
for x in range(5):
    board.append(["O"] * 5)

# the next few lines draws the board on the console
def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

# the next few lines hide the ship in the board!
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# comment out next two lines while playing as they display the location of the ship
print (ship_row)
print (ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent!

for turn in range(4):
   guess_row = int(input("Guess Row:"))
   guess_col = int(input("Guess Col:"))


# TO DO: write condition to test for correct guesses 
   if (guess is correct):
        print ("Congratulations! You sunk my battleship!")
        break
   else:
# TO DO: write condition for guesses outside the board
        if (guess is outside board):
            print ("Oops, that's not even in the ocean.")
# TO DO: write condition for repeated guess
        elif (already guessed that spot):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            #Set location to “X”
    if turn == 3 :
        print ("Game Over")

    # TO DO:
    # write conditional statements to check for the following conditions:
    # is the guess correct?
    # has the location been guessed already?
    # is the guess out of bounds?
    # is the guess wrong?
    # when the guess is wrong, replace guessed location on the board with an “X”
    # NOTE: use the “break” command to exit the loop when the guess is correct
    # NOTE: make sure to keep track of the number of turns remaining
