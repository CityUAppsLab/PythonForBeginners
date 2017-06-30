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
 
play = True #starts the game loop
 
while play:
    #resets the board
    theBoard = [' '] * 10
    valid_moves = ["1","2","3","4","5","6","7","8","9"]
    print("Welcome to Tic Tac Toe! Player 1 goes first.")
    #initialize necessary variables
    player = 1
    game = True  
 
    while game:
        #TODO:take in user input 
        player_input = input(“Question goes here”)
        #check if the move is valid 
        if player_input in valid_moves:
             #TODO: Mark the board with the necessary mark (“X” or “O”) 
 
             if player == 1:
                  #TODO
                  #add the move onto the board
                  #remove player_input from list of valid_moves
                  #check if player has won
                  if winner(theBoard, “O”):
                        #TODO: What happens when a player wins?
             else:
                 #TODO: repeat similar steps from player 1 for player 2
 
             #print the board to the console
             drawBoard(theBoard)
        else:
            print("Invalid input. Try again")
        
        #TODO: Should end game if someone won or there are not more valid moves
        #after game over, ask if players want to play again
        if (input("play again? y/n") == "n"):
            play = False
            print(“Thanks for playing!”)
