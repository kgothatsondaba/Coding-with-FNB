
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press 'q' to quit: ")
    if food.lower() == 'q':
        break
    try:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)
    except ValueError:
        print("Please enter a valid number for the price.")

print("----- YOUR CART -----")

for food in foods:
    print(food, end =  " ")

for price in prices:
    total += price

print("\n")
print(f"Your total is: R{total:}")
