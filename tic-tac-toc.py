def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def winner(board, player):
    # board variable is the list of the gameboard
    # player is the player's symbol ("O" or "X")
    # TO DO:
    # return true if a player has three in a row, 
    # horizontally, vertically or diagonally
    # else, return false
    # hint, use boolean operators (“==”) and logical operators (“and”, “or”)

play = True # starts the game loop


while play:
    # Reset the board and start game
    theBoard = [' '] * 10
    valid_moves = ['1','2','3','4','5','6','7','8','9']
    labels = ['0','1','2','3','4','5','6','7','8','9']
    print("Welcome to Tic Tac Toe! Player 1 goes first.")
    drawBoard(labels)

    # Initialize necessary variables
    player = 1
    game = True

    while game:
        # Take in user input
        player_input = input("Input your move: ")
        # Check if the move is valid
        if player_input in valid_moves:
             #Mark the board with the necessary mark (“X” or “O”)
             if player == 1: # For player 1: O
                  # TO DO:
                  # add the move onto the board
                  # remove player_input from list of valid_moves
                  # change the player number
                  # check if player has won
                  if winner(theBoard, "O"):
                        # TO DO: What happens when a player wins? 
                        # Remember to draw the board!
                        break # leaves current loop
                  else:
                      print('Player 2\'s turn!')
             else: # For player 2: X
                 # TO DO: repeat similar steps from player 1 for player 2
                 # Add move, remove from list of valid_moves, check for winner etc.
                 if winner(theBoard, "X"):
                       # TO DO: What happens when a player wins?
                       # Very similar to player 1
                       break
                 else:
                     print('Player 1\'s turn !')

             # Print the board to the console
             drawBoard(theBoard)
        else:
            print("Invalid input. Try again")

        # End game if someone won or there are not more valid moves (draw)
        # After game over, ask if players want to play again
        if(len(valid_moves)==0): #checks if there's a draw, no more moves left
            # TO DO: print "Draw" message and end game

    if (input("play again? y/n") == "n"):
        play = False
        print("Thanks for playing!")
