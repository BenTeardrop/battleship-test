import random

if __name__ == "__main__":
    print('Battleship')
    

def board():
  pass


def players_choice():
    your_choice_row = input('Choose your row: ')
    your_choice_column = input('Choose your column: ')
    row_choice = int(your_choice_row)
    column_choice = int(your_choice_column)
    your_coordinates = column_choice, row_choice 
    print(your_coordinates)
    return your_coordinates
    

def computers_choice():
    comp_choice_row = random.randint(0,8)
    comp_choice_column = random.randint(0,8)
    comp_coordinates = comp_choice_row, comp_choice_column
    # for comp_coordinate in comp_coordinates
    print(comp_coordinate)
    return comp_coordinates

def players_ship():
    players_ship_row = random.randint(1,8) 
    players_ship_column = random.randint(1,8) 
    players_ship_coordinates = players_ship_row, players_ship_column
    print(players_ship_coordinates)
    return players_ship_coordinates

def computer_ship():
    computer_ship_row = random.randint(1,8)
    computer_ship_column = random.randint(1,8)
    computer_ship_coordinates = computer_ship_row, computer_ship_column
    print(computer_ship_coordinates)
    return computer_ship_coordinates




players_shot = players_choice()  
computer_coordinate = computer_ship()
computer_shot = computers_choice()
players_coordinate = players_ship()

def players_turn(players_shot, computer_coordinate):
    score = 0
    score_max = 5
    while (score < 5):
    
        if players_shot == computer_coordinate:
            score += 1
            print("one ship Down!")
        else:
            print("miss!!")
            break

players_turn(players_shot, computer_coordinate)


# def random_coordinate():
#     x = random.randint(0,8)
#     y = random.randint(0,8)
#     print(x,y)

# board()
# random_spot = random_coordinate()
