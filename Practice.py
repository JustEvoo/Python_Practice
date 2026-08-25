
menu = {"Pizza": 3.50,
        "Burger": 4.50,
        "Pasta": 15.50}
cart = []
total = 0
print("=" * 100)
print(f"{"Welcome to the menu":^100}")
print("=" * 100)
for key, value in menu.items():
    print(f"{key:7}: ${value:.2f}")
print("-" * 100)

while True:
    food = input("Select an option (q to quit): ").capitalize()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(total)