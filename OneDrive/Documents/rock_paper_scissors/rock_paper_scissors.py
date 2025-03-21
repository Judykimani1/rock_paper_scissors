plays = ["rock","paper","scissors"]
player = input("Enter either of the following(rock, paper or scissors): ").lower()
if player not in plays:
    print("Invalid input. Game over!")
else:
    import random
    computer = random.choice(plays)
    print(f"Computer played {computer}. Player played {player}.")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("rock smashes scissors. You win!")
        else:
            print("paper covers rock. You lose!")
    elif player == "paper":
        if computer == "rock":
            print("paper covers rock. You win!")
        else:
            print("scissors cuts paper. You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("scissors cuts paper. You win!")
        else:
            print("rock smashes scissors. You lose!")
    else:
        print("Invalid input. Game over")
# End of rock_paper_scissors.py


