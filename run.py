import random

if __name__ == "__main__":
    print('Battleship')
    
#initializing board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))


def players_choice():
    your_choice_row = input('Choose your row: ')
    your_choice_column = input('Choose your column: ')
    row_choice = int(your_choice_row)
    column_choice = int(your_choice_column)
    your_coordinates = row_choice, column_choice
    print(your_coordinates)
    return your_coordinates
    

def computers_choice():
    comp_choice_row = random.randint(1,5)
    comp_choice_column = random.randint(1,5)
    comp_coordinates = comp_choice_row, comp_choice_column
    for comp_coordinate in comp_coordinates:
        print(comp_coordinate)
    return comp_coordinates

def players_ship():
    players_ship_row = random.randint(1,5) 
    players_ship_column = random.randint(1,5) 
    players_ship_coordinates = players_ship_row, players_ship_column
    print(players_ship_coordinates)
    return players_ship_coordinates

def computer_ship():
    # computer_ship_row = random.randint(1,8)
    # computer_ship_column = random.randint(1,8)
    # computer_ship_coordinates = computer_ship_row, computer_ship_column
    computer_ship_coordinates = 2, 3
    print(computer_ship_coordinates)
    return computer_ship_coordinates





def players_turn(players_shot, computer_coordinates):
    score = 0
    score_max = 5
    while (score < 5):
    
        if players_shot == computer_coordinates:
            score += 1
            print("one ship Down!")
        elif score == 5:
            print('you Win!')
            break
        else:
            print("miss!!")
print_board(board)
players_shot = players_choice()  
computer_coordinates = computer_ship()
computer_shot = computers_choice()
players_coordinate = players_ship()
players_turn(players_shot, computer_coordinates)




# def random_coordinate():
#     x = random.randint(0,8)
#     y = random.randint(0,8)
#     print(x,y)

# board()
# random_spot = random_coordinate()

