import art
import random


the_board = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

spaces_taken = []
game_is_on = True
move_number = 0


def validate_entry():
    entry = input("Choose your spot: ")
    if entry in spaces_taken:
        print("That spot is taken. Choose another spot:")
        return validate_entry()
    elif entry.isnumeric():
        spaces_taken.append(entry)
        return entry
    elif entry.upper() == "EXIT":
        return entry
    else:
        print("Please enter a numeric value from 1 to 9.")
        return validate_entry()


def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def choose_player():
    choice = input("Do you want to play as 'X' or 'O'? ")
    if choice.upper() == "X":
        return ["X", "O"]
    elif choice.upper() == "O":
        return ["O", "X"]
    else:
        print("Invalid entry. Please enter a letter - either 'X' or 'O'.")
        return choose_player()


def check_turn_order():  # Player goes on odd turns and AI on even
    if move_number % 2 == 0:
        return "computer"
    else:
        return "player"


def make_move(board, letter, move):
    board[move] = letter


def check_for_winner(board, letter):
    if (board['1'] == letter and board['2'] == letter and board['3'] == letter) or \
       (board['4'] == letter and board['5'] == letter and board['6'] == letter) or \
       (board['7'] == letter and board['8'] == letter and board['9'] == letter) or \
       (board['1'] == letter and board['4'] == letter and board['7'] == letter) or \
       (board['2'] == letter and board['5'] == letter and board['8'] == letter) or \
       (board['3'] == letter and board['6'] == letter and board['9'] == letter) or \
       (board['3'] == letter and board['5'] == letter and board['7'] == letter) or \
       (board['1'] == letter and board['5'] == letter and board['9'] == letter):
        return True


def get_comp_move():  # This is where the computer AI goes
    comp_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    if comp_choice in spaces_taken:
        return get_comp_move()
    else:
        spaces_taken.append(comp_choice)
        return comp_choice


def continue_game():
    answer = input("Play again? Type 'Y' or 'N': ").upper()
    if answer == 'Y':
        # Clears the board
        for key in the_board:
            the_board[key] = ' '
        spaces_taken.clear()
        move_number = 0
        return True, move_number
    elif answer == 'N':
        move_number = 0
        return False, move_number
    else:
        "Invalid entry. Please try again."
        return continue_game()

print(art.demo)
player_side, comp_side = choose_player()



while game_is_on:
    move_number += 1
    turn = check_turn_order()
    if turn == "player":
        player_entry = validate_entry()
        if player_entry.upper() == "EXIT":
            game_is_on = False
        make_move(board=the_board, letter=player_side, move=player_entry)
        print_board(the_board)
        if check_for_winner(board=the_board, letter=player_side):
            print("Congratulations! You win!")
            game_is_on, move_number = continue_game()
    elif turn == "computer":
        print("Computer is thinking...")
        comp_entry = get_comp_move()
        make_move(board=the_board, letter=comp_side, move=comp_entry)
        print_board(the_board)
        if check_for_winner(board=the_board, letter=comp_side):
            print("Sorry, you lose.")
            game_is_on, move_number = continue_game()



