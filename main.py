import random

board = ["-","-", "-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "X" 
winner = None
gameRunning = True #loop is controlled by this global variable; =True to start it off


def printBoard(board): 
    print(board[0] + " | " + board[1] + " | " + board[2]) #print each row
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    valid = False
    while not valid: #keep asking until a valid move is made
        inp = int(input("Enter a number 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer #set this position = to the currentPlayer ('X')
            valid = True
        else:
            print("Opponent is already at that spot.. 😫 Try again!")

def checkHorizontle(board):
    # global means if we make changes to the winner variable within the scope of this function, the winner variable changes within the scope of the entire file
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False # to ensure that the 'winner' doesn't change if it isn't a winner

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[1]
        return True
    return False

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

def checkForWin():
    global gameRunning
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False

def switchPlayer(): #don't pass an argument because we are not going to make any modifications to the board
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Create a computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkForWin()
    checkTie(board)
    if not gameRunning:
        break # Exit the loop if the game has ended
    switchPlayer()
    computer(board)
    checkForWin()
    checkTie(board)



