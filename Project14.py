import random
import time

# Slot symbols
slot_symbols = ["🍒", "🍋", "🍊", "🍉", "🍇", "🔔", "⭐", "💎"]

def spin_slots():
    return [random.choice(slot_symbols) for _ in range(3)]

def display_slots(slots):
    print("\nSpinning...")
    time.sleep(1)
    print(" | ".join(slots))
    print()
    if slots[0] == slots[1] == slots[2]:
        print("🎉 You win! 🎉")
    else:
        print("💔 You lose. 💔")

def calculate_winnings(slots, bet):
    if slots[0] == slots[1] == slots[2]:
        symbol = slots[0]
        if symbol == "💎":
            print(f"Jackpot! 💰 You won {bet * 10:.2f}")
            return bet * 10
        elif symbol == "⭐":
            print(f"Awesome! You won {bet * 5:.2f}")
            return bet * 5
        elif symbol == "🔔":
            print(f"Nice! You won {bet * 3:.2f}")
            return bet * 3
        else:
            print(f"You won {bet * 2:.2f}")
            return bet * 2
    return 0

def get_deposit():
    while True:
        try:
            amount = float(input("Enter your initial deposit amount: "))
            if amount <= 0:
                print("❌ Please enter a positive amount.")
            else:
                return amount
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def get_bet(balance):
    while True:
        bet = input("Enter your bet amount (or type 'exit' to return to main menu): ")
        if bet.lower() == 'exit':
            return None
        if not bet.isdigit():
            print("❌ Please enter a valid positive number.")
            continue
        bet = int(bet)
        if bet <= 0:
            print("❌ Bet must be greater than zero.")
        elif bet > balance:
            print("❌ You don’t have enough balance.")
        else:
            return bet

def main():
    print("🎰 Welcome to the Slot Machine Game 🎰")
    balance = get_deposit()

    while True:
        print("\n--- Main Menu ---")
        print("1. Spin the Slots")
        print("2. Check Balance")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            while True:
                bet = get_bet(balance)
                if bet is None:
                    break  # return to main menu
                balance -= bet
                slots = spin_slots()
                display_slots(slots)
                winnings = calculate_winnings(slots, bet)
                balance += winnings
                print(f"💰 Current balance: {balance:.2f}")
                if balance <= 0:
                    print("⚠️ You have run out of money. Game over!")
                    return
        elif choice == "2":
            print(f"💰 Your current balance is: {balance:.2f}")
        elif choice == "3":
            print("👋 Thank you for playing! Goodbye!")
            break
        else:
            print("❌ Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
