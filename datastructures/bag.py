from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.bag_list = []
        self.bag_dict = {}

    def add(self, item: T) -> None:
        if item is not None:
            if item in self.bag_list:
                    self.bag_dict[item] += 1
            else:
                self.bag_list.append(item)
                self.bag_dict[item] = 1
        else:
            raise TypeError("Wrong Value")

    def remove(self, item: T) -> None:
        if item in self.bag_list and item in self.bag_dict:
            if self.bag_dict[item] > 1:
                self.bag_dict[item] -= 1
            
            elif self.bag_dict[item] == 1:
                self.bag_dict.pop(item)
                self.bag_list.pop(item)
        else:
            raise ValueError(item, "is not in the list.")

    def count(self, item: T) -> int:
        if item in self.bag_list:
            return self.bag_dict[item]
        else:
            return 0

    def __len__(self) -> int:
        all_items_in_dict = 0

        for items in self.bag_list:
            all_items_in_dict += self.bag_dict[items]

        return all_items_in_dict

    def distinct_items(self) -> int:
        diff_items = len(self.bag_list)

        return set(self.bag_list)

    def __contains__(self, item) -> bool:
        if item in self.bag_list:
            return True
        
        else:
            return False

    def clear(self) -> None:

        self.bag_list.clear()
        
        self.bag_dict.clear()
