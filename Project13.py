#Banking Program

balance = 10000
def show_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited: ${amount:.2f}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrew: ${amount:.2f}")
def show_main_menu():
    print("Main Menu:")
    print("1. Show Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    isrunning = True
    while isrunning:
        match input("Choose an option (1-4): "):
            case '1':
                show_balance()
            case '2':
                amount = float(input("Enter amount to deposit: "))
                deposit(amount)
            case '3':
                amount = float(input("Enter amount to withdraw: "))
                withdraw(amount)
            case '4':
                print("Thank you for using the Banking Program!")
                isrunning = False
            case _:
                print("Invalid option, please try again.")
                continue
def main():
    print("Welcome to the Banking Program!")
    show_main_menu()

if __name__ == "__main__":
    main()
               
