- My menu_list is an Array because it's size is never going to change during the order of the costumer.

- The same goes for the bistro_menu. It's a 2D-array with the drinks as rows and it's properties as colums (name, prize, size). 

- When the costumer orders/personalizes their drink I add the drink with its properties (as a list) to another list. I'm ending up with a new 2D-list (order) - same structre as my bistro_menu.

- I tried to implement my order-list as an array at first, but then I gave up, because that list also has to able to grow dynamically. I don't want to restrict my customers from ordering more. I WANT MONEY!

- Then I display the whole order as a receipt, with the prize and the total amount of the order. 

- My hidden_order list is the list of the order containing all the details about the drinks. 

        - order: a list that contains the properties of the personalized drink
        - hidden order: is a list organized as a queue - FIFO
        - ready_for report: a 3D list that contians all oders as a separate item in a list (the order is a 2D list with all the drinks ordered as item, and the drinks are list themselves.) => A list within a list within a list. This list is also organized as a queue. The items inside represent the string representation of all the open orders. As soon as an order gets marked off, I just pop of the last order (next item getting dequed of a list) and put them in my daily report bag, since they've been ready for report. 
        - open_order: a 1D list of strings representing the open orders with the name and the drinks with all the sizes. 

- At first I wanted to implement my open_orders as an actual queue, but my open_order queue wasn't displaying my orders nicely, because my str()-function in array.py is not optimzed to just print the important items. I also changed my open order queue to a list because it has to be able to grow dynamically. But I implemented a function (append_to_front) that takes in an item and a list and appends the item at the front and returns a new list. Then when I remove an order I just pop the last item/person of that list. FIFO system. 

- My end_of_day report is a Bag. I chose this data structure because it stores every item indivudally and keeps the different items separated and adds 1 to the counter when the Item is alerady in there. Then when I print out the bag, it just returns all unique drinks (it seperates them from sizes as well). The bag doesn't return 0 if one of the drinks hasn't been sold, because that drink has never been in the bag. The bag only returns the items that are or have been in the bag.


- I didn't get to use as many Array based data strucutures because they would restrict the costumers from ordering different amounts of drinks. 

- The reason for setting hidden_orders equal to an empty list, is that clear() doesn't work. For some reason ready_for_report gets cleared as well whenever we clear hidden_orders. So professor Cordova and I tried with setting it equal to an empty list, and it started working.  