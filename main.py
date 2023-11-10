import random

def user_choice():
    while True:
        try:
            ui_number = int(input("1: Rock, 2: Paper, 3: Scissors -- "))
            if ui_number > 3 or ui_number < 1:
                print("Podaj liczbe od 1 do 3")
                continue
            break
        except ValueError: print("Podaj liczbe od 1 do 3")
    if ui_number == 1:
        ui_choice = "Rock"
    elif ui_number == 2:
        ui_choice = "Paper"
    else: ui_choice = "Scissors"
    return ui_choice

def determine_winner(ui_choice: int, bot_choice: str):
    if ui_choice == bot_choice:
        return None
    elif ui_choice == "Rock" and bot_choice == "Scissors":
        return True
    elif ui_choice == "Scissors" and bot_choice == "Paper":
        return True
    elif ui_choice == "Paper" and bot_choice == "Rock":
        return True
    return False

def game():
    choices = ["Rock", "Paper", "Scissors"]
    bot_choice = random.choice(choices)

    ui_choice = user_choice()
    you_win = determine_winner(ui_choice, bot_choice)

    if you_win:
        print(f"Your choice: {ui_choice}, Bot choice {bot_choice}")
        print("You win! :) +1 point for You!")
        winner = "User"
    elif you_win is None:
        print(f"Your choice: {ui_choice}, Bot choice {bot_choice}")
        print("It's a tie - 0 points")
        winner = None
    else:
        print(f"Your choice: {ui_choice}, Bot choice {bot_choice}")
        print("Bot wins! :( +1 point for Bot!")
        winner = "Bot"
    return winner

def main():
    while True:
        try:
            rounds = int(input("How many rounds?: "))
            break
        except ValueError: print("Podaj poprawną liczbe")
    points = []
    for round in range(rounds):
        print(f"Round {round+1}")
        winner = game()
        points.append(winner)
        print("Score:")
        print(f"User: {points.count('User')} points, Bot {points.count('Bot')} points")
        print()
    if points.count('User') > points.count('Bot'):
        print("The winner of the game is YOU!!!")
    elif points.count('User') == points.count('Bot'):
        print("It's a TIE, try again")
    else: print("The winner of the game is BOT!!! try again :(") 
main()