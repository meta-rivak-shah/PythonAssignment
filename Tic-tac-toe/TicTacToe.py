from random import randint
import time

#function is used to print the bord after every chance
def printBoard(board):
            print("|[",board[0],"] 0| [",board[1],"]  1|  [",board[2],"]  2|",end ="  \n")
            print("|[",board[3],"] 3| [",board[4],"]  4|  [",board[5],"]  5|",end ="  \n")
            print("|[",board[6],"] 6| [",board[7],"]  7|  [",board[8],"]  8|",end ="  \n")


#function is used to check that game is complete or not
def boardIsNotFilled(board):
    count = 0
    for symbol in board:
        if(symbol is not '0'):
            count += 1
        if(count == len(board)):
            return False
        else:
            return True

#function is used to check that there is any values exit on that path
def checkSymbolPlaceOnPath(path):
    if(board[path] is not '0'):
        return True
    return False

#check that symbol exit in these all path path1 path2 path3
def checkSymbolOnPath(path1 , path2 , path3 , symbol):
    if(board[path1] is symbol and board[path2] is symbol and board[path3] is symbol):
        return True
    return False
#check the game winner by passing all the path one by one
def checkGameWinner(symbol):
    if(checkSymbolOnPath(0,1,2 ,symbol) is True):
        return True
    elif(checkSymbolOnPath(3,4,5 ,symbol) is True):
        return True
    elif(checkSymbolOnPath(6,7,8 ,symbol) is True):
        return True
    elif(checkSymbolOnPath(0,4,8 ,symbol) is True):
        return True
    elif(checkSymbolOnPath(2,4,6 ,symbol) is True):
        return True
    elif(checkSymbolOnPath(0,3,6 ,symbol) is True):
        return True
    elif(checkSymbolOnPath(1,4,7 ,symbol) is True):
        return True
    elif(checkSymbolOnPath(2,5,8 ,symbol) is True):
        return True
    return False

#for user input we have these functionality
def userFunctionality(userSymbol):

    userPath = int(input("select any path"))
    while(checkSymbolPlaceOnPath(userPath) is True):
        print("There is allready a symbol placed at another position for user")
        userPath = int(input("select any path"))
    board[userPath]  = userSymbol
    if(checkGameWinner(userSymbol) is True):
        print("User Win the Game")
        return True
    return False
#for cpu input we have the functionality
def  cpuFunctionality(computerSymbol):
    cpuPath = randint(0,8) #take any random value between 0 to 8
    while(checkSymbolPlaceOnPath(cpuPath) is True):
        print("There is allready a symbol placed at another position for cpu")
        cpuPath = randint(0,9)  
        board[cpuPath] = computerSymbol
    if(checkGameWinner(computerSymbol) is True):
        print("Cpu Win the Game")
        return True
    return False

board = [
        '0','0','0',
        '0','0','0',
        '0','0','0' 
]

print("Welcome to tic-tac-toe Game")
time.sleep(2)
print("your tic tac toe board is here")
printBoard(board)
print("SELECT YOUR Symbol X Or Y")
userSymbol = input("Enter your Symbol")

if(userSymbol.upper() == 'X'):
    computerSymbol = 'Y'
else:
    computerSymbol = 'X'
userSymbol = userSymbol.upper()

while(boardIsNotFilled(board) is True):
    try:
       if(userFunctionality(userSymbol) is True or cpuFunctionality(computerSymbol) is True):
            break
       printBoard(board)
    except Exception:
        print("insert only integer value please again start the game")
    
    
printBoard(board)
