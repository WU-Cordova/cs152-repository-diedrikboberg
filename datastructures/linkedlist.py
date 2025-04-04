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
            llist.append(item)

        return llist



    def append(self, item: T) -> None:

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
        new_node = LinkedList.Node(data = item)

        new_node.next = self.head

        if self.head:
            self.head.previous = new_node

        self.head = new_node

        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        # raise value error if the target does not exst
        # raise typeerror if the target is not the right type
        #rase tvpeerror if the item is not the right type

        travel = self.head

        while travel:

            if travel.data == target:
                break

            travel = travel.next

        if travel is None:
            raise ValueError(f"The target value {target} was not found in the list.")
        
        if travel is self.head: #about the object not the value
            self.prepend(item)

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
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

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
        raise NotImplementedError("LinkedList.pop_front is not implemented")

    @property
    def front(self) -> T:
        raise NotImplementedError("LinkedList.front is not implemented")

    @property
    def back(self) -> T:
        ...

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

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
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

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
