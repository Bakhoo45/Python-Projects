#Dice Roller Program

import random
#● ┌ ┐ ─ │ └ ┘
dice_dic = {1: ("┌─────┐\n│     │\n│  ●  │\n│     │\n└─────┘"),
            2: ("┌─────┐\n│●    │\n│     │\n│    ●│\n└─────┘"),
            3: ("┌─────┐\n│●    │\n│  ●  │\n│    ●│\n└─────┘"),
            4: ("┌─────┐\n│●   ●│\n│     │\n│●   ●│\n└─────┘"),
            5: ("┌─────┐\n│●   ●│\n│  ●  │\n│●   ●│\n└─────┘"),
            6: ("┌─────┐\n│●   ●│\n│●   ●│\n│●   ●│\n└─────┘")}
def roll_dice():
    roll = random.randint(1, 6)
    print(dice_dic[roll])
    print(f"You have rolled a {roll}!\n")

def main():
    while True:
        user_input = input("Press yes to roll the dice or no to quit: ")
        if user_input.lower() == 'no':
            print("Thanks for playing!")
            break
        elif user_input.lower() == 'yes':
           roll_dice()
        else:
            print("Invalid input, please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()