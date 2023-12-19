from time import sleep
import numpy
import os
import keyboard

def menu():
    option = -1

    while option == -1:
        print("\t\t7x7 TicTacToe\n")
        print("1. Begin a game")
        print("2. Leaderboard") # sort all players by their max wins
        print("3. View & sort players") # allow to view all players, also to sort by their scores, turns, asc. desc. etc.
        print("4. Find player data") # to-do
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

def balance_grid_navigation(arr, xy = [0, 0]):

    if(xy[1] >= len(arr[0])): # max y is 7 but our y is >7
        xy[1] = 0 # y to leftmost

    if(xy[1] < 0): # min y is 0 but our y is < 0
        xy[1] = len(arr[0]) - 1 # y to rightmost
        
    if(xy[0] >= len(arr)): # max x is 7 but our x is >7
        xy[0] = 0 # x to top

    if(xy[0] < 0): # min x is 0 but our x is < 0
        xy[0] = len(arr) - 1 # x to bottom

    return xy

def select_grid(arr, msg='', highlighter='-'):
    cursor = [0, 0]

    while True:
        os.system('cls')
        display_grid(arr, highlighter, cursor)
        print(msg)

        if keyboard.is_pressed("right"):
            cursor = balance_grid_navigation(arr, [cursor[0], cursor[1] + 1])
        if keyboard.is_pressed("left"):
            cursor = balance_grid_navigation(arr, [cursor[0], cursor[1] - 1])
        if keyboard.is_pressed("up"):
            cursor = balance_grid_navigation(arr, [cursor[0] - 1, cursor[1]])
        if keyboard.is_pressed("down"):
            cursor = balance_grid_navigation(arr, [cursor[0] + 1, cursor[1]])
        if keyboard.is_pressed("enter"):
            return cursor

        sleep(0.07)

def game_start(player1, player2):
    grid = numpy.array([['-' for y in range(7)] for x in range(7)])
    display_grid(grid)

    turns = 0
    while any('-' in arr for arr in grid):
        
        player = '-'
        if turns % 2 == 0:
            player = 'X'
        else:
            player = 'O'

        position = select_grid(grid, f"Player [{player}]: Use arrows to select and 'ENTER' key to place at the '+'", '+')

        if grid[position[0], position[1]] != '-':
            print("\nERROR: You cannot place here!")
            sleep(1.5)
            continue
        else:
            grid[position[0], position[1]] = player
            turns = turns+1
            print("\nSUCCESS: Placed!")

            # check for winning...
            sleep(1)
    # exhausted all attempts

menu()