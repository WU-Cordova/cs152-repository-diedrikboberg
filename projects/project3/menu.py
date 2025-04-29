from datastructures.array import Array
from datastructures.array2d import Array2D
from datastructures.bag import Bag
from datastructures.circularqueue import CircularQueue


menu_list = Array(["Display Menu", "Take New Order", "View Open Orders", "Mark Next Order as Complete", "view End-Of-Day report", "Exit"], str)
bistro_menu = Array2D([["Mocha Latte", 3.49, "S"],["Cappuchino", 2.99, "S" ],["Frappuchina", 4.99, "S"],["Latte", 2.15, "S"],["Vanilla Milkshake",5.99, "S"]])
order = []
open_orders = []
hidden_orders = []
end_of_day_report = Bag()

def add_to_front(item, ordered_list):
    new_list = []
    new_list.append(item)
    for item2 in ordered_list:
        new_list.append(item2)

    return new_list


def display_menu():
    for i in range(len(bistro_menu)):
        print(f"{i+1}. {bistro_menu[i][0]}: ${bistro_menu[i][1]}")

    print("------------------------")

print("welcome to the Bearcat Bistro!")
print("-------------------------------")
for i in range(len(menu_list)):
    print(f"{i + 1}. {menu_list[i]}")
    print((len(menu_list[i])+3)*"-")

while True:
    

    choice = input("Please select an option (1-6): ")

    # Show menu
    if choice == "1":
        print("All drinks available:")
        print("----------------------")
        display_menu()
    
    # New order
    elif choice == "2":
        sum = 0

        order_amount = int(input("Please enter the amount of the drinks you would like to order: "))
        for i in range(order_amount):
            drink = int(input(f"Drink #{i+1}: ")) - 1
            order.append(bistro_menu[drink])

        
        name = input("Please enter your name: ")
        name += ": "

        print("Your order:")
        for i in range(len(order)):
            name += f"{order[i][0]} [{order[i][2]}] "
            sum += order[i][1]
            print(f"\n{order[i][0]} {order[i][2]}: ${order[i][1]}")
        
        for i in range(len(order)):
            hidden_orders.append(order[i])

        order.clear()
        open_orders = add_to_front(name, open_orders)
        
        print("------------------------")
        print(f"Total: {sum}\n")
        
        
    # View open orders
    elif choice == "3":
        print("Open Orders:")
        for order4 in open_orders[::-1]:
            print(order4)
        
        print(hidden_orders)
        

        
        
    elif choice == "4":
        #to_end_of_day = hidden_orders[::1]
        #end_of_day_report.add(to_end_of_day)
        open_orders.pop()

        print("Hidden Orders:")
        for order in hidden_orders:
            text_order = f"{order[0]} [{order[2]}]"
            #print(order[0], order[2])
            #hidden_orders.remove(order)
            end_of_day_report.add(text_order)
        print(hidden_orders)
        

    elif choice == "5":
        print(end_of_day_report)
        
    elif choice == "6":
        print("Thank you for visiting the Bearcat Bistro!")
        print("Goodbye!")
        break
