#!/usr/bin/python
# This is a program for a very simple Connect Four game simulation.
# The human player will always go first.
# The computer's moves are randomly generated.
# When there is a winner, an appropriate message is output and the program
# terminates.
import random
import time

# This function will display the game board
def display(matrix):
    print("1 2 3 4 5 6 7")
    for row in matrix:
        print(' '.join(map(str,row)))

# This function will randomly generate the computer's move and place it on
# the board
def compMove(matrix):
    filled = False
    valid = False
    c = random.randint(0,7)
    c = c - 1
    r = 5
    while not valid:
        if matrix[0][c] != '-' and matrix[1][c] != '-' and\
        matrix[2][c] != '-' and matrix[3][c] != '-' and\
        matrix[4][c] != '-' and matrix[5][c] != '-' :
            cl = random.randint(0,7)
            if cl == c + 1:
                valid = False
            else:
                c = cl
                c = c - 1
                valid = True
        else:
            valid = True
                
    while not filled:
        if matrix[r][c] == '-':
            matrix[r][c] = 'C'
            filled = True
            return matrix
        else:
            r = r - 1
            filled = False

            

# This function will get input from the human player and place
# the move on the board
def humMove(matrix):
    c = int(input("Input the column number (1-7) for your move: "))
    c = c - 1
    filled = False
    valid = False
    r = 5
    while not valid:
        if matrix[0][c] != '-' and matrix[1][c] != '-' and\
        matrix[2][c] != '-' and matrix[3][c] != '-' and\
        matrix[4][c] != '-' and matrix[5][c] != '-':
            cl = int(input("This column is full. Choose another: "))
            if cl == c + 1:
                valid = False
            else:
                c = cl
                c = c - 1
                valid = True
        else:
            valid = True
        
    while not filled:
        if matrix[r][c] == '-':
            matrix[r][c] = 'H'
            filled = True
            return matrix
        else:
            r = r - 1
            filled = False

# This function will check to see if someone has won
def win(matrix):
    # Checking columns
    for c in range(0,7):
        for r in range(0,3):
            if matrix[r][c] == matrix[r + 1][c] == matrix[r + 2][c] ==\
            matrix[r + 3][c] and matrix[r][c] != '-':
                if matrix[r][c] == 'C':
                    print("The computer has won!")
                    return True
                elif matrix[r][c] == 'H':
                    print("You have won!")
                    return True

    # Checking rows
    for r in range(0,6):
        for c in range(0,3):
            if matrix[r][c] == matrix[r][c + 1] == matrix[r][c + 2] ==\
            matrix[r][c + 3] and matrix[r][c] != '-':
                if matrix[r][c] == 'C':
                    print("The computer has won!")
                    return True
                elif matrix[r][c] == 'H':
                    print("You have won!")
                    return True



    # Checking diagonals from top to bottom, left to right
    for r in range(0,3):
        for c in range(0,4):
            if matrix[r][c] == matrix[r + 1][c + 1] ==\
            matrix[r + 2][c + 2] == matrix[r + 3][c + 3] and\
            matrix[r][c] != '-':
                if matrix[r][c] == 'C':
                    print("The computer has won!")
                    return True
                elif matrix[r][c] == 'H':
                    print("You have won!")
                    return True


    # Checking diagonals from bottom to top, left to right
    for r in range(5, 2, -1):
        for c in range(0,3):
            if matrix[r][c] == matrix[r - 1][c + 1] ==\
            matrix[r - 2][c + 2] == matrix[r - 3][c + 3] and\
            matrix[r][c] != '-':
                if matrix[r][c] == 'C':
                    print("The computer has won!")
                    return True
                elif matrix[r][c] == 'H':
                    print("You have won!")
                    return True

    return False  

# This is the main game function
def game():
    rows, cols = 6, 7
    
    print("Thanks for playing Connect Four!")          
    print("You will make the first move.")
    again = 'Y'
    while again == 'Y' or again == 'y':
        matrix = [['-' for x in range(cols)] for y in range(rows)]
        num = 0
        while num < 46:
            display(matrix)
            print(" ")
            humMove(matrix)
            print(" ")
            display(matrix)
            print(" ")
            if win(matrix) is True:
                break
            print("The computer is contemplating its move...")
            time.sleep(3)
            compMove(matrix)
            print(" ")
            if win(matrix) is True:
                break
        again = input("Play again (Y/N)? ")


# Calls main game function in order to begin the game
game()
