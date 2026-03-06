def add_item(cart_list, item):
    cart_list.append(item)
    print(f"Added {item} to the cart.")


def calculate_total(cart_list, price_dictionary):
    total = 0
    

    for item in cart_list:

        total += price_dictionary.get(item, 0)
    

    if total > 100:
        print(f"Original total: ${total}. Applying 10% discount!")
        total = total * 0.90  
    else:
        print(f"Total is ${total}. Spend over $100 for a discount.")
        
    return total


def main():
    # Dictionary to store prices
    item_prices = {
        "shoes": 60,
        "jacket": 50,
        "hat": 20
    }
    
    # List to keep track of added items
    shopping_cart = []
    
    # Adding items
    add_item(shopping_cart, "shoes")
    add_item(shopping_cart, "jacket")
    

    final_price = calculate_total(shopping_cart, item_prices)
    
    print(f"Your final price is: {final_price:.2f} PKR")



main()
