from random import randint
def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    moves = ['rock', 'paper', 'scissors']
    random_move = randint(0, 2)
    computer_choice = moves[random_move]
    print(computer_choice)
    if player_choice == computer_choice:
        print ('Draw!')
    elif moves=='rock' and computer_choice == 'scissors':
        win()
    elif  player_choice == 'paper' and computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
    elif player_choice == 'rock' and computer_choice == 'paper':
        win()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    again = input('Do you want to play again? (y or n)')
    if again == 'y':
        continue
    else:
        break


# import random

# while True:
#     choices = ["rock","paper","scissors"]
#     camputer = random.choice(choices)
#     player=0
#     while player not in choices:
#         player=input("rock , paper or scissors:=").lower()
#     if player==camputer:
#         print("camputer",camputer)
#         print("player",player)
#         print("draw")
#     elif player=="rock":
#         if camputer=="paper":
#             print("camputer",camputer)
#             print("player",player)
#             print("you lose")
#         if camputer=="scissors":
#             print("camputer",camputer)
#             print("player",player)
#             print("you win!")
#     elif player=="scissors":
#         if camputer=="rock":
#             print("camputer",camputer)
#             print("player",player)
#             print("you lose")
#         if camputer=="paper":
#             print("camputer",camputer)
#             print("player",player)
#             print("you win!")
#     elif player=="paper":
#         if camputer=="scissors":
#             print("camputer",camputer)
#             print("player",player)
#             print("you lose")
#         if camputer=="rock":
#             print("camputer",camputer)
#             print("player",player)
#             print("you win!")
#     again = input('Do you want to play again? (y or n)')
#     if again == 'n':
#         break


