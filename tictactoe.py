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
        print("3. Exit")
        option = int(input("\nSelect an option: "))
        print()

    if option == 1:
        player1 = input("Enter Player [X] name: ")
        player2 = input("Enter Player [O] name: ")

        game_start(player1, player2)
    elif option == 2:

        print('\nDisplaying leaderboard:')
        with open("winners.txt", "r") as file:
            lines = file.readlines()

            unique_winners = []
            winner_counts = []

            for line in lines:
                winner = line.strip() # remove \n (new line character) at the end of name of winner

                if winner in unique_winners:
                    index = unique_winners.index(winner)
                    winner_counts[index] += 1
                else:
                    unique_winners.append(winner)
                    winner_counts.append(1)

            n = len(unique_winners)

            for i in range(n): # bubble sort to sort winners and count
                for j in range(0, n-i-1):
                    if winner_counts[j] < winner_counts[j+1]:
                        winner_counts[j], winner_counts[j+1] = winner_counts[j+1], winner_counts[j]
                        unique_winners[j], unique_winners[j+1] = unique_winners[j+1], unique_winners[j]

            for i in range(len(unique_winners)):
                print(f"{unique_winners[i]}: {winner_counts[i]} times")
        
        input('\nPress ENTER to go back to the menu...\n')
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        return 5
    else:
        print("Invalid option! Going back to the menu...")
        sleep(2)
        menu()

    return -1

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
        os.system('clear')
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

def game_win(winner):
    print(f'\n{winner} has won! (4 successive placements)')

    with open('winners.txt', 'a') as file:
        file.write(winner + '\n')

    sleep(3)

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

            # check for win in x axis (left-right)
            successive = 0
            
            for i in range(position[0]-4, position[0]+4):
                if i < 0 or i >= len(grid):
                    continue

                if grid[i, position[1]] == player:
                    successive = successive + 1
                    
                    if successive == 4:
                        break
                else:
                    successive = 0

            if successive == 4:
                game_win(player1 if player == 'X' else player2)
                return
            
            # check for win in y axis (up-down)
            successive = 0
            
            for i in range(position[1]-4, position[1]+4):
                if i < 0 or i >= len(grid[0]):
                    continue

                if grid[position[0], i] == player:
                    successive = successive + 1
                    if successive == 4:
                        break
                else:
                    successive = 0

            if successive == 4:
                game_win(player1 if player == 'X' else player2)
                return

            # check for win in primary diagonal
            successive = 0
            for i in range(-3, 4):
                row, col = position[0] + i, position[1] + i
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    if grid[row, col] == player:
                        successive += 1
                        if successive == 4:
                            break
                    else:
                        successive = 0

            if successive == 4:
                game_win(player1 if player == 'X' else player2)
                return

            # check for win in secondary diagonal
            successive = 0
            for i in range(-3, 4):
                row, col = position[0] + i, position[1] - i
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    if grid[row, col] == player:
                        successive += 1
                        if successive == 4:
                            break
                    else:
                        successive = 0

            if successive == 4:
                game_win(player1 if player == 'X' else player2)
                return
            

    # exhausted all attempts
    print(f'\nStalemate! No one won!')
    sleep(3)
    

while True:
    if menu() == 5:
        break