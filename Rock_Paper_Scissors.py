import random

# This function lists the options in which the player can choose.

def play():
    user = input("What's your choice?\n 'rock' for Rock, 'paper' for Paper, 'scissors' for Scissors:\n ")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return "It's a tie"

    # r > s, s > p, p > r   
    if is_win(user, computer):
        return "You Won!"
    
    return "You Lost! :("

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') \
        or (player == 'paper' and opponent == 'rock'):
        return True

print(play())