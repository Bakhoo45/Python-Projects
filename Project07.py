#Shopping Cart

food = []
price = []
total = 0

while True:
    item = input("Enter the food item (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    food.append(item)
    
    cost = float(input(f"Enter the price for {item}: "))
    price.append(cost)
    total += cost

print("\nShopping Cart:")
for i in range(len(food)):
    print(f"{food[i]}: ${price[i]:.2f}")
print(f"Total: ${total:.2f}")
