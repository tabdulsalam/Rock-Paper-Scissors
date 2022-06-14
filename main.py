import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper-> paper wins \n"
      + "Rock vs scissor-> Rock wins \n"
      + "paper vs scissor-> scissor wins \n")


while True:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)

    player = False

    while player == False:
        player = input("Enter choice \n R for Rock, \n P for paper and \n S for scissor \nPlayer: ").upper()

        if player == computer:
            print(f"Player ({player}) : CPU ({computer})")
            print("Tie!")

        elif player == "R":
            if computer == "P":
                print(f"Player ({player}) : CPU ({computer})")
                print("CPU win! You lose!")
            if computer == "S":
                print(f"Player ({player}) : CPU ({computer})")
                print("You win! CPU lose!")

        elif player == "S":
            if computer == "R":
                print(f"Player ({player}) : CPU ({computer})")
                print("CPU win! You lose!")
            if computer == "P":
                print(f"Player ({player}) : CPU ({computer})")
                print("You win! CPU lose!")

        elif player == "P":
            if computer == "S":
                print(f"Player ({player}) : CPU ({computer})")
                print("CPU win! You lose!")
            if computer == "R":
                print(f"Player ({player}) : CPU ({computer})")
                print("You win! CPU lose!")
        else:
            print("ERROR! That's not a valid play.")

    play_again = input("Play again? Enter (yes / no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
