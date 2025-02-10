from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.bag_list = []
        self.bag_dict = {}
        self.bag_tot = []

        for item in items:
            self.add(item)
    
    def dictionary(self):
        for items in self.bag_dict:
            print("keys:",self.bag_dict.keys(),"Value:", self.bag_dict[items])

    def add(self, item: T) -> None:
        if item is not None:
            print("adding",item)
            self.bag_tot.append(item)
            print(len(self.bag_tot))
            if item in self.bag_list:
                self.bag_dict[item] += 1

            else:
                self.bag_list.append(item)
                self.bag_dict[item] = 1


            print("Added item.\n")
        else:
            raise TypeError("Wrong Value")

    """
    def remove(self, item: T) -> None:
        print(self.bag_tot)
        if item in self.bag_tot:
            self.bag_tot.remove(item)
            if self.bag_dict[item] > 1:
                self.bag_dict[item] -= 1
            
            elif self.bag_dict[item] == 1:
                self.bag_dict.pop(item)
                self.bag_list.remove(item)
        else:
            raise ValueError(item, "is not in the list.")
    """


    def remove(self, item: T) -> None:
        #print(self.bag_tot)  # Debugging - ensure this is necessary

        if item in self.bag_tot:
            print("1 card removed...")
            self.bag_tot.remove(item)

            if item in self.bag_dict:  # Ensure item exists in bag_dict before accessing
                if self.bag_dict[item] > 1:
                    self.bag_dict[item] -= 1
                else:
                    self.bag_dict.pop(item)

            if item in self.bag_list:  # Ensure item is in bag_list before removing
                self.bag_list.remove(item)
        else:
            raise ValueError(f"{item} is not in the list.")




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
        #return diff_items

    def __contains__(self, item) -> bool:
        if item in self.bag_list:
            return True
        
        else:
            return False

    def clear(self) -> None:

        self.bag_list.clear()
        
        self.bag_dict.clear()
    
    # I know this is going to have a big impact on the big O notation, since I generate a long list every time I call this method

    def generate_all(self):
        """
        all = []
        for key in self.bag_dict:
            for item in range(self.bag_dict[key]):
                all.append(key)
        
        return all
        """
        return self.bag_tot

    def take(self, item):
        #self.generate_all().remove(item)
        self.remove(item)
        return self.generate_all