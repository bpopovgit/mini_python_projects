import random
from colorama import Fore, Style

player_score = 0
computer_score = 0

while True:
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'

    player_decision = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_decision.lower() == "r":
        player_decision = rock
    elif player_decision.lower() == "p":
        player_decision = paper
    elif player_decision.lower() == "s":
        player_decision = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    computer_random_number = random.randint(1, 3)
    computer_decision = ""

    if computer_random_number == 1:
        computer_decision = rock
    elif computer_random_number == 2:
        computer_decision = paper
    elif computer_random_number == 3:
        computer_decision = scissors

    print(f"{Fore.BLUE}The computer chose {computer_decision}.")

    if (player_decision == rock and computer_decision == scissors)\
            or (player_decision == paper and computer_decision == rock)\
            or (player_decision == scissors and computer_decision == paper):
        print(Fore.GREEN + "You win!")
        player_score += 1
    elif (player_decision == rock and computer_decision == paper)\
            or (player_decision == paper and computer_decision == scissors)\
            or (player_decision == scissors and computer_decision == rock):
        print(Fore.RED + "You lose!")
        computer_score += 1
    else:
        print(Fore.YELLOW + "Draw!")

    print()
    print(f"{Fore.GREEN}Your score: {player_score}")
    print(f"{Fore.RED}Opponent's score: {computer_score}")
    print(Style.RESET_ALL)

    restart_game = input("Type [yes] to Play Again or [no] to quit: ")

    if restart_game.lower() == "yes":
        continue
    elif restart_game.lower() == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Exiting...")
        exit()