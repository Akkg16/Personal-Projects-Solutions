import random

def play():
    user_input = input("Rock 'r', scissors 's' paper 'p'  ")
    computer = random.choice(['r','p','s'])
    if user_input == computer:
        return "It's a tie"
    if who_wins(user_input, computer):
        return "You won!"
    else:
        return "You lost"
   
def who_wins(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())   