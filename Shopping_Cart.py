#Shoping Cart Program by AITMAD


cart = ["Apple", "Milk", "Bread", "Chocolate"]


price_map = {
    "Apple": 30,
    "Milk": 90,
    "Bread": 50,
    "Chocolate": 120
}

total_cost = 0


for item in cart:
    total_cost += price_map.get(item, 0)


if total_cost > 100:
    discount = total_cost * 0.10  # 10% discount
    total_cost -= discount
    print(f"Discount applied! Your new total is: {total_cost} PKR")
else:
    print(f"Total: {total_cost} PKR")
