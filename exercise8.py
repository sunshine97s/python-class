# Rock Paper Scissors game
user_1 = input("Player 1, please enter your name: ")
user_2 = input("Player 2, please enter your name: ")

def winner_choice():
    choice1 = input("Player 1, pick your choice: ")
    choice2 = input("Player 2, pick your choice: ")
    winner = ""
    if choice1 == choice2:
        print("You tied")
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            print(user_1 + " wins! ")
            winner = user_1
        else:
            print(user_2 + " wins!")
            winner = user_2
    elif choice1 == 'scissors':
        if choice2 == 'paper':
            print(user_1 + " wins! ")
            winner = user_1
        else:
            print(user_2 + " wins!")
            winner = user_2
    elif choice1 == 'paper':
        if choice2 == 'rock':
            print(user_1 + " wins!")
            winner = user_1
        else:
            print(user_2 + " wins!")
            winner = user_2

    return winner

for x in range(1, 4):
    print(winner_choice())
