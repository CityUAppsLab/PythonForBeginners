from random import randint

#empty board list
board = []

#the next few lines generate an empty board
for x in range(5):
    board.append(["O"] * 5)

#the next few lines draws the board on the console
def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

#the next few lines hide the ship in the board!
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


#you may comment the next two lines while playing as they display the location of the ship
#print (ship_row)
#print (ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent!
history = []

def guess(row,col):

    if(row == ship_row and col == ship_col):
        return 'correct'

    elif(row > 4 or col > 4 or row < 0 or col < 0):
        return 'outside_board'

    elif [row, col] in history:
        return 'already_guessed'

for turn in range(4):

   guess_row = int(input("Guess Row(0-4):"))
   guess_col = int(input("Guess Col(0-4):"))

   #checks if guess is correct
   if guess(guess_row, guess_col) is 'correct':
        print ("Congratulation s! You sunk my battleship!")
        break

  #checks if guess is outside the board
   elif guess(guess_row, guess_col) is 'outside_board':
        print ("Oops, that's not even in the ocean.")

  #checks if guess has already been guessed
   elif guess(guess_row, guess_col) is 'already_guessed':
        print ("You guessed that one already.")

   else:
        print ("You missed my battleship!")
        history.append([guess_row,guess_col])
        board[guess_row][guess_col] = "X"

   print_board(board)

   #ends game
   if turn == 3:
        print ("Game Over")
