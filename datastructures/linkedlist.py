from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterator, Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


# yield - saves state of function, gives a function a memory - doesn't break the loop

class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.count = 0
        self.head  = self.tail = None
        self.data_type = data_type


    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        llist: LinkedList[T] = LinkedList(data_type= data_type)

        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError(f"{item}, is has the wrong type.")
            
            llist.append(item)

        return llist



    def append(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"{item} has the wrong type.")
        node = LinkedList.Node(data = item)

        if self.empty:
            self.head = self.tail = node

        else:
            # set node's previous to tail
            node.previous = self.tail
            # set tail's next to new node
            if self.tail:
                self.tail.next = node
            # set tail to the new node
            self.tail = node

        self.count += 1



    def prepend(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"{item} has the wrong type.")
        new_node = LinkedList.Node(data = item)

        if self.empty:
            self.head = self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node 

        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        # raise value error if the target does not exst
        # raise typeerror if the target is not the right type
        #rase tvpeerror if the item is not the right type
        if not isinstance(item, self.data_type):
            raise TypeError(f"{item} has the wrong type.")
        
        if not isinstance(target, self.data_type):
            raise TypeError(f"{target} has the wrong type.")

        travel = self.head

        while travel:

            if travel.data == target:
                break

            travel = travel.next

        if travel is None:
            raise ValueError(f"The target value {target} was not found in the list.")
        
        if travel is self.head: #about the object not the value
            self.prepend(item)

        else:
            new_node = LinkedList.Node(data=item)
            new_node.previous = travel.previous
            new_node.next = travel
            travel.previous.next = new_node
            travel.previous = new_node
            self.count += 1
        #not the head

        # 1. create new node
        # 2. set travel.previous = new_node
        # 3. set travel.previous.next = new_node

        # or

        # 1. create new node
        # 2. set travel.previous.next = new_node
        # 3. new_node.next = travel
        
        #backwards
        # 4. new_node.previous = travel.previous
        # 5. travel.previous = new_node

            

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"item: {item} has the wrong type.")
        
        if not isinstance(target, self.data_type):
            raise TypeError(f"target: {target} has the wrong type.")
        
        travel = self.head
        while travel:
            if travel.data == target:
                break
            travel = travel.next
        if travel is None:
            raise ValueError(f"Target: {target} is of the wrong value")
        
        new_node = LinkedList.Node(data=item)

        new_node.previous = travel
        new_node.next = travel.next
        if travel.next:
            travel.next.previous = new_node

        else:
            self.tail = new_node
        travel.next = new_node
        self.count += 1
        

    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"{item} has the wrong type.")
        
        travel = self.head
        while travel:
            if travel.data == item:
                if travel.previous:
                    travel.previous.next = travel.next
                else:
                    self.head = travel.next
                if travel.next:
                    travel.next.previous = travel.previous
                else:
                    self.tail = travel.previous
                self.count -= 1
                return
            travel = travel.next
        raise ValueError(f"item:{item} not found in list")
    

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"{item} has the wrong type.")
        
        travel = self.head
        while travel:
            next_node = travel.next
            if travel.data == item:
                if travel.previous:
                    travel.previous.next = travel.next
                else:
                    self.head = travel.previous
                self.count -= 1
            travel = next_node

    def pop(self) -> T:
        if self.tail is None:
            raise IndexError("List is empty!")
        
        data = self.tail.data
        self.count -= 1

        if self.head is not self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
            return data
        
        elif self.head is self.tail:
            self.head = self.tail = None

        return data


        





    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("LL is empty.")
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        self.count -= 1
        return data

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("LL is empty.")
        return self.head.data
    

    @property
    def back(self) -> T:
        if self.empty:
            raise IndexError("LL is empty.")
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.head = self.tail = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        travel = self.head
        while travel:
            if travel.data == item:
                return True
            travel = travel.next
        return False

    def __iter__(self) -> Iterator[T]: # returns an iterator
        self._travel_node = self.head
        return self

    def __next__(self) -> T:
        if self._travel_node is None:
            raise StopIteration("Iteration stopped")
        
        data = self._travel_node.data
        self._travel_node = self._travel_node.next

        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        self.travel_node = self.tail
        while self.travel_node:
            yield self.travel_node.data
            self.travel_node = self.travel_node.previous
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if self.count != other.count:
            return False
        current_self = self.head
        current_other = other.head
        while current_self and current_other:
            if current_other.data != current_other.data:
                return False
            current_other = current_other.next
            current_self = current_self.next
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
