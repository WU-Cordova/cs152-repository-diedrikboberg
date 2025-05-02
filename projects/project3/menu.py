from datastructures.array import Array
from datastructures.array2d import Array2D
from datastructures.bag import Bag
from datastructures.circularqueue import CircularQueue
import time


menu_list = Array(["Display Menu", "Take New Order", "View Open Orders", "Mark Next Order as Complete", "view End-Of-Day report", "Exit"], str)
bistro_menu = Array2D([["Prepper", 3.49, "S"],["Chill Bearcat", 2.99, "S" ],["Mr.Studious", 4.99, "S"],["Blitz's Favorite", 2.15, "S"],["Vanilla Milkshake",5.99, "S"]])
order = []
open_orders = []
hidden_orders = []
ready_for_report = []
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

def get_last_list(day_report):
    return day_report[-1]

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

            new_order = []
            for i in range(3):
                new_order.append(bistro_menu[drink][i])
            
            size = input("S for small , M for medium (+$0.5), L for large (+$1): ").upper()
                
            if size == "S":
                pass
            elif size == "M":
                new_order[1] += 0.50
                new_order[2] = "M"
            elif size == "L":
                new_order[1] += 1.00
                new_order[2] = "L"

    
            order.append(new_order)
            #new_order.clear()

        name = input("Please enter your name: ")
        name += ": "

        print("Your order:")
        for i in range(len(order)):
            name += f"{order[i][0]} [{order[i][2]}] "
            sum += order[i][1]
            print(f"\n{order[i][0]} {order[i][2]}: ${order[i][1]}")

            print("------------------------")
            print(f"Total: {round(sum,2)}\n")
        
        yes_no = input("Is this order correct? (Y/N): ").upper()
        if yes_no == "N":
            print("Order cancelled.")
            order.clear()
            
            continue

        else:
        #for i in range(len(order)):
            #hidden_orders.append(order[i])
            for item in order:
                hidden_orders = add_to_front(item, hidden_orders)
        
        
            ready_for_report = add_to_front(hidden_orders, ready_for_report)
            #hidden_orders.append(order)
            order.clear()
            hidden_orders = []
            open_orders = add_to_front(name, open_orders)
            
        

    # View open orders
    elif choice == "3":
        if len(open_orders) == 0:
            print("No open orders.")
            continue
        print("Open Orders:")
        for order4 in open_orders[::-1]:
            print(order4)
        
        #print(hidden_orders)
        #print("Ready for report:", ready_for_report)
             
    # Mark next order as complete
    elif choice == "4":
        #to_end_of_day = hidden_orders[::1]
        #end_of_day_report.add(to_end_of_day)
        if len(open_orders) == 0:
            print("No open orders to mark as complete.")
            continue

        print("Marking next order as complete...")
        time.sleep(2)
        
        open_orders.pop()

        to_get_reported = get_last_list(ready_for_report)
        #print("Hidden Orders:")
        for order2 in to_get_reported:
            text_order = f"{order2[0]} [{order2[2]}]"
            #print(order[0], order[2])
            #hidden_orders.remove(order)
            end_of_day_report.add(text_order)

        ready_for_report.pop()
        print("Order marked as complete.")

        #print("Ready for report:", ready_for_report)
        
    # View end-of-day report
    elif choice == "5":
        if len(end_of_day_report) == 0:
            print("No orders have been made so far.")
            continue    
        print("End of Day Report:")
        print("------------------------")
        print(end_of_day_report)
        
    # Exit
    elif choice == "6":

        print("Exiting the Bearcat Bistro...")
        time.sleep(2)
        print("")
        print("Thank you for visiting the Bearcat Bistro!")
        print("")
        time.sleep(1)
        print("Goodbye!")
        time.sleep(5)
        break
