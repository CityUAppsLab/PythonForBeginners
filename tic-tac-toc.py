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
    #TODO
    #this function returns true if a player has three in a row, horizontally, vertically or diagonally
    #else, return false
    #hint, use boolean operators (“==”, “and”, “or”)
    if(board[1] == player and board[2] == player and board[3] == player ):
      return True
    elif(board[4] == player and board[5] == player and board[6] == player):
      return True
    elif(board[7] == player and board[8] == player and board[9] == player):
      return True
    elif(board[1] == player and board[4] == player and board[7] == player):
      return True
    elif(board[3] == player and board[6] == player and board[9] == player):
      return True
    elif(board[2] == player and board[5] == player and board[8] == player):
      return True
    elif(board[1] == player and board[5] == player and board[9] == player):
      return True
    elif(board[3] == player and board[5] == player and board[7] == player):
      return True
    else:
      return False


play = True #starts the game loop


while play:
    #resets the board
    theBoard = [' '] * 10
    valid_moves = ['1','2','3','4','5','6','7','8','9']
    labels = ['0','1','2','3','4','5','6','7','8','9']
    player1 = []
    player2 = []
    print("Welcome to Tic Tac Toe! Player 1 goes first.")
    #initialize necessary variables
    drawBoard(labels)
    player = 1
    game = True

    while game:
        #TODO:take in user input
        player_input = input("Input your move: ")
        #check if the move is valid
        if player_input in valid_moves:
             #TODO: Mark the board with the necessary mark (“X” or “O”)

             if player == 1:
                  #TODO
                  #add the move onto the board
                  #remove player_input from list of valid_moves
                  #check if player has won
                  valid_moves.remove(player_input)
                  theBoard[int(player_input)]='O'
                  player = 2
                  if winner(theBoard, "O"):
                        #TODO: What happens when a player wins?
                        print('Player1 wins!')
                        drawBoard(theBoard)
                        break
                  else:
                      print('Player2\'s turn!')
             else:
                 #TODO: repeat similar steps from player 1 for player 2
                 valid_moves.remove(player_input)
                 theBoard[int(player_input)]="X"
                 player = 1
                 if winner(theBoard, "X"):
                       #TODO: What happens when a player wins?
                       print('Player2 wins!')
                       drawBoard(theBoard)
                       break
                 else:
                     print('Player1\'s turn !')

             #print the board to the console
             drawBoard(theBoard)
        else:
            print("Invalid input. Try again")

        #TODO: Should end game if someone won or there are not more valid moves
        #after game over, ask if players want to play again
        if(len(valid_moves)==0):
            print("Draw!")
            game = False

    if (input("play again? y/n") == "n"):
        play = False
        print("Thanks for playing!")
