#Rock Paper Scissors Game
import random
choices  = {"rock 🪨 ": 1 , "paper 📃 ": 2, "scissors ✂️ ": 3}
def play_round():
    user_choice = int(input("Enter 1 for rock 🪨, 2 for paper 📃, or 3 for scissors ✂️  :  "))
    computer_choice = random.choice(list(choices.keys()))
    print(f"Computer chose : {computer_choice:2} and you chose : {list(choices.keys())[user_choice - 1]}")
    if user_choice == choices[computer_choice]:
        print("It's a tie!")
    elif (user_choice == 1 and choices[computer_choice] == 3) or \
         (user_choice == 2 and choices[computer_choice] == 1) or \
         (user_choice == 3 and choices[computer_choice] == 2):
        print("You win!")
    else:
        print("You lose!")

def main():
    print("Welcome to Rock Paper Scissors!")
    while True:
        play_round()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            continue
        elif play_again == 'no':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input, exiting the game.")
            break
        

if __name__ == "__main__":
    main()