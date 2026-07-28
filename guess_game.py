# ==========================================
# Ultimate Number Guessing Game
# Python Mini Project
# ==========================================


import random
import os
import datetime



# ==========================================
# Save Score
# ==========================================


def save_score(name, score, attempts):

    date = datetime.datetime.now()

    with open("leaderboard.txt", "a") as file:

        file.write(
            f"{name} | Score: {score} | Attempts: {attempts} | {date}\n"
        )



# ==========================================
# Show Leaderboard
# ==========================================


def show_leaderboard():

    print("\n========== LEADERBOARD ==========")


    try:

        with open("leaderboard.txt", "r") as file:

            data = file.readlines()


            if data:

                for player in data:

                    print(player.strip())


            else:

                print("No scores available")


    except FileNotFoundError:

        print("No leaderboard found")




# ==========================================
# Select Difficulty
# ==========================================


def difficulty_level():


    print("\nSelect Difficulty")

    print("1. Easy   (1-50, 10 Attempts)")
    print("2. Medium (1-100, 7 Attempts)")
    print("3. Hard   (1-500, 5 Attempts)")


    while True:

        try:

            choice = int(input("Choose level: "))


            if choice == 1:

                return 50,10


            elif choice == 2:

                return 100,7


            elif choice == 3:

                return 500,5


            else:

                print("Invalid Choice")


        except ValueError:

            print("Enter a number")




# ==========================================
# Game Function
# ==========================================


def play_game():


    print("\n==============================")
    print("   ULTIMATE GUESSING GAME")
    print("==============================")


    name = input("\nEnter your name: ")



    max_number, max_attempts = difficulty_level()



    secret_number = random.randint(
        1,
        max_number
    )



    score = max_attempts * 100


    attempts = 0



    print(
        f"\nGuess number between 1 and {max_number}"
    )


    while attempts < max_attempts:


        try:


            guess = int(
                input("Your guess: ")
            )


            attempts += 1



            if guess == secret_number:


                score = score - (attempts-1)*10


                print("\n🎉 Correct Guess!")

                print(
                    f"Attempts Used: {attempts}"
                )


                print(
                    f"Your Score: {score}"
                )


                save_score(
                    name,
                    score,
                    attempts
                )


                break



            elif guess < secret_number:


                print("⬆ Too Low")



            else:


                print("⬇ Too High")



            remaining = max_attempts - attempts


            print(
                f"Remaining Attempts: {remaining}"
            )



        except ValueError:


            print(
                "Please enter valid number"
            )



    else:


        print("\n❌ Game Over")

        print(
            f"The number was {secret_number}"
        )



# ==========================================
# Main Menu
# ==========================================


def main():


    while True:


        print("\n==============================")

        print("  NUMBER GUESSING GAME MENU")

        print("==============================")

        print("1. Play Game")

        print("2. Leaderboard")

        print("3. Exit")



        choice = input(
            "Choose option: "
        )



        if choice == "1":


            play_game()



        elif choice == "2":


            show_leaderboard()



        elif choice == "3":


            print(
                "Thanks for playing!"
            )

            break



        else:


            print(
                "Invalid Option"
            )



# Run Program

main()