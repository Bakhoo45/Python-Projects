#Concession Stand Program

menu = {
    "hot_dog": 3.50,
    "hamburger": 4.00,
    "soda": 1.50,
    "nachos": 2.50,
    "popcorn": 2.00,
    "candy": 1.00
}

cart = []
total_cost = 0.0
print("Welcome to the Concession Stand!")
for key, value in menu.items():
    print(f"{key.title():10}: ${value:.2f}")
print("-----------------------------------")

while True:
    food_item = input("Enter a food item to add to your cart (or 'done' to finish): ").lower()
    if food_item == "done":
        break
    if food_item in menu:
        cart.append(food_item)
        total_cost += menu[food_item]
    else:
        print("Item not found in menu.")

print("-----------------------------------")
print("Your cart contains:")
for item in cart:
    print(f"{item.title():10}: ${menu[item]:.2f}")
print(f"{'Total':10}: ${total_cost:.2f}")