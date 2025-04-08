"""
Food Ordering System
A simple console-based application for restaurant management
"""

# Food Menu Database
menu = [
    {"id": 1, "name": "Vegetable biryani", "price": 299},
    {"id": 2, "name": "Panner biryani", "price": 319},
    {"id": 3, "name": "Mushroom biryani", "price": 349},
    {"id": 4, "name": "Egg biryani", "price": 329},
    {"id": 5, "name": "Chicken biryani", "price": 399},
]

orders = []

def display_menu():
    print("\n==== Menu ====")
    print("{:<5} {:<20} {:<10}".format("ID", "Item", "Price"))
    for item in menu:
        print("{:<5} {:<20} RS{:<9.2f}".format(
            item["id"], 
            item["name"], 
            item["price"], 
        ))

def take_order():
    display_menu()
    order_items = []
    
    while True:
        try:
            item_id = int(input("\nEnter item ID to order (0 to finish): "))
            if item_id == 0:
                break
            item = next((x for x in menu if x["id"] == item_id), None)
            
            if item:
                quantity = int(input(f"Enter quantity for {item['name']}: "))
                if quantity > 0:
                    order_items.append({
                        "item": item,
                        "quantity": quantity,
                        "total": item["price"] * quantity
                    })
                    print(f"{quantity}x {item['name']} added to order!")
                else:
                    print("Quantity must be at least 1")
            else:
                print("Invalid item ID! Please try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    if order_items:
        orders.append(order_items)
        print("\nOrder placed successfully!")
        display_order_summary(order_items)

def display_order_summary(order_items):
    total = 0
    print("\n==== Order Summary ====")
    for item in order_items:
        print(f"{item['quantity']}x {item['item']['name']} - ${item['total']:.2f}")
        total += item['total']
    print(f"Total: ${total:.2f}")

def order_history():
    print("\n==== Order History ====")
    for i, order in enumerate(orders, 1):
        print(f"Order {i}:")
        display_order_summary(order)

def main():
    print("Welcome to Food Ordering System!")
    
    while True:
        print("\nOptions:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Order History")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_menu()
        elif choice == '2':
            take_order()
        elif choice == '3':
            order_history()
        elif choice == '4':
            print("Thank you for using our system!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
