import random 
import string
choice = ["k", "p", "n", "q"]
user_win = 0
computer_win = 0
while True:
    user_choice = input("Wybierz kamień/papier/nożyce wpisując odpowiednio 'k' 'p' 'n' lub 'q' jeśli chcesz wyjść: ").lower()
    if user_choice not in choice:
        print("Not a valid choice.")
        continue
    user_choice1 = user_choice
    if user_choice1 == "k":
        info1 = "kamień"
    elif user_choice1 == "p":
        info1 = "papier"
    else:
        info1 = "nożyce"
    computer_choice = random.randint(0,2)
    computer_choice = choice[computer_choice]
    computer_choice1 = computer_choice
    if computer_choice == "k":
        info = "kamień"
    elif computer_choice == "p":
        info = "papier"
    elif computer_choice == "n":
        info = "nożyce"
    if user_choice == "q":
        break
    else:
        print(".")
        print(".")
        print(".")
        print("You have chosen", info1 , "and the computer has chosen", info ,"")
        if (user_choice == "k" and computer_choice == "n") or (user_choice == "n" and computer_choice == "p") or (user_choice == "p" and computer_choice == "k"):
            print("You won!")
            user_win = user_win + 1
            continue
        elif (user_choice == computer_choice):
            print("It's a draw!")
            computer_win = computer_win + 1
            continue
        else:
            print("You lose!")
print("You have won", user_win ,"times, and the computer has won", computer_win ,"times.")
if user_win > computer_win:
    print("You rock, keep it up!")
elif user_win < computer_win:
    print("You suck, get better bruh")
else:
    user_win = computer_win
    print("Nothing to be happy about..")
print("Thanks for playing")
        


    