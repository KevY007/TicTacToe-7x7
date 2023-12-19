from time import sleep
import numpy
import os
import keyboard

def menu():
    option = -1

    while option == -1:
        print("\t\t7x7 TicTacToe\n")
        print("1. Begin a game")
        print("2. View scores")
        print("3. View players")
        print("4. Find player data")
        option = int(input("\nSelect an option: "))
        print()

    if option == 1:
        player1 = input("Enter Player [X] name: ")
        player2 = input("Enter Player [O] name: ")

        game_start(player1, player2)
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        print("Invalid option! Going back to the menu...")
        sleep(2)
        menu()

def display_grid(arr, highlighter = '-', highlight = [-1, -1]):
    print('\nGrid: ')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if x == highlight[0] and y == highlight[1]:
                print(highlighter, end=' ')
            else:
                print(f'{arr[x][y]}', end=' ')
        print()
    print()

def select_grid(arr, msg='', highlighter='-'):
    begin = [0, 0]

    while True:
        os.system('cls')
        display_grid(arr, highlighter, begin)
        print(msg)

        if keyboard.is_pressed("right"):
            begin[1] = begin[1] + 1
            
        elif keyboard.is_pressed("left"):
            begin[1] = begin[1] - 1
        elif keyboard.is_pressed("up"):
            begin[0] = begin[0] - 1
        elif keyboard.is_pressed("down"):
            begin[0] = begin[0] + 1
        elif keyboard.is_pressed("enter"):
            break

        sleep(0.1)
    
    pass

def game_start(player1, player2):
    grid = numpy.array([['-' for y in range(7)] for x in range(7)])
    display_grid(grid)

    select_grid(grid, "Player [X]: Use arrows to select and 'F' key to place", 'X')
    pass

menu()