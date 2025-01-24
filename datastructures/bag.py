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
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> int:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")