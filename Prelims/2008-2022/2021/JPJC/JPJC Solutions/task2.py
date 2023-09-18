#Server socket
#=============
import random, socket

def InitialiseGrid():
    grid = [["O"] * 5] * 4  #4 rows by 5 columns grid for battleship
    for i in range(4):      #to avoid aliasing
            grid[i] = ["O"] * 5
    return grid

def DisplayGrid(grid):
    for row in grid:
        cs.sendall(("\t".join(row)+"\n").encode())    
    cs.sendall(b"\n")

def getInput():
    while True:
        cs.sendall(b"Enter row number (0 to 3):\n") #instruction to enter number
        row = cs.recv(1024).decode() #receives number from client
        row = int(row)
        if ValidateRow(row):
            break

    #TASK 1
    while True:    
        cs.sendall(b"Enter col number (0 to 4):\n")
        col = cs.recv(1024).decode()
        col = int(col)
        if ValidateCol(col):
            break

    return (row, col)

def ValidateRow(row): #range check only
    return row >= 0 and row <= 3

def ValidateCol(col): #range check only
    return col >= 0 and col <= 4

def CheckResult(row, col):
    if ship_row == row and ship_col == col: #player guessed correctly
        grid[row][col] = "S"
        return True
    else:
        grid[row][col] = "X" #player guessed wrongly
        return False
        
    
#MAIN PROGRAM
#============
ss = socket.socket()
ss.bind(('127.0.0.1',6789))
ss.listen()

cs, addr = ss.accept() #establish connection with client

#Program a battleship game using the functions and procedures coded
#Player has three guesses.

ship_row = random.randint(0,3)
ship_col = random.randint(0,4)
print(ship_row, ship_col)
number_guesses = 0

grid = InitialiseGrid()
cs.sendall(b"Welcome to Battleship!\n")

while number_guesses < 3: #player makes up to three guesses
    DisplayGrid(grid)    
    row, col = getInput()  
    won = CheckResult(row, col)
    
    if won == True:
        DisplayGrid(grid)
        cs.sendall(b"YOU WON!\n")
        break
    
    number_guesses += 1

if won == False:
    DisplayGrid(grid)
    cs.sendall(b"GAME OVER...")

cs.close()
ss.close()
       
    
