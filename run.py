import random

if __name__ == "__main__":
    print('Battleship')

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    """
    prints the board
    """
    for row in board:
        print (" ".join(row))

def generate_random_coordinate():
    """
    Generates 2 random coordinates
    """
    row = random.randint(1,5)
    column = random.randint(1,5)
    return (row, column)


def players_choice():
    """
    player choice of row and column
    """
    your_choice_row = input('Choose your row: ')
    your_choice_column = input('Choose your column: ')
    row_choice = int(your_choice_row)
    column_choice = int(your_choice_column)
    your_coordinates = row_choice, column_choice
    if row_choice and column_choice > 5:
        print('stay below 5')
        players_choice()
    print(f'your shot:{your_coordinates}')
    return your_coordinates
    

def computers_choice():
    """
    computers choice of coordinates to hit the boat
    """
    comp_coordinates = generate_random_coordinate()
    print(f'comps Shot :{comp_coordinates}')
    return comp_coordinates

# def players_ship():
#     """
#     players ship coordinates
#     """
#     players_ship_coordinates = generate_random_coordinate()
#     print(players_ship_coordinates)
#     return players_ship_coordinates

# def computer_ship():
#     """
#     computer ship coordinates
#     """
#     computer_ship_coordinates = generate_random_coordinate()
#     print(computer_ship_coordinates)
#     return computer_ship_coordinates

def generate_my_ship_coordinates():
    coordinates_list = []
    for x in range(0,5):
        ship_coordinates = generate_random_coordinate()
        coordinates_list.append(ship_coordinates)
    print(f'my ships coordinates: {coordinates_list}')
    return coordinates_list

def generate_computers_ship_coordinates():
    coordinates_list = []
    for x in range(0,5):
        ship_coordinates = generate_random_coordinate()
        coordinates_list.append(ship_coordinates)
    print(f'computers ships coordinates: {coordinates_list}')
    return coordinates_list

def mark_board_with_ship_coordinates():
    global board
    coordinates_list = generate_my_ship_coordinates()
    for coordinate in coordinates_list:
        row, column = coordinate
        board[row-1][column-1] = '@'

def mark_board_with_computer_hits():
    global board
    computers_hits = int(computers_turn(computer_shot, my_ship_coordinates))
    for coordinate in computers_hits:
        row, column = coordinate
        board[row-1][column-1] = 'x'
        



def players_turn(players_shot, computer_coordinates):
    score = 0
    score_max = 5
    while (score < 5):
        if players_shot in comp_coordinates:
                score += 1
                print(score)
                print("computer Ship Down!")
                print(f'score:{score}')
                players_choice()
        elif score == 5:
            print('you Win!')
            break
        else:
            print("computer ship missed!!")
            players_choice()
            
            

def computers_turn(computer_shot, my_ship_coordinates):
    if computer_shot in my_ship_coordinates:
        print("players Ship down!!!")
    else:
        print("players ship miss!!!")
my_ship_coordinates = generate_my_ship_coordinates()
mark_board_with_ship_coordinates()     
print_board(board)
comp_coordinates = generate_computers_ship_coordinates()
# generate_random_coordinate()
players_shot = players_choice()  
# computer_coordinates = computer_ship()
computer_shot = computers_choice()
# players_coordinate = players_ship()
players_turn(players_shot, comp_coordinates)
computers_turn(computer_shot, my_ship_coordinates)
# mark_board_with_computer_hits()




# def random_coordinate():
#     x = random.randint(0,8)
#     y = random.randint(0,8)
#     print(x,y)

# board()
# random_spot = random_coordinate()
