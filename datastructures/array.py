# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


#uneccesdf
from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None:
        
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Entered sequence is not a sequence.")
        
        for element in starting_sequence:
            if not isinstance(element, data_type):
                raise TypeError("Your data types are not the same.")

        
        #if type()

        
        self.my_array = np.array(starting_sequence)

        self.my_logivcal_s = len(self.my_array)

        self.my_physical_s = 2**self.my_logivcal_s.bit_length()

        self.d_type = data_type

        print(self.d_type)
        #while item in starting_sequence:
            #self.my_array.append(item)
        #self.my_array = np.array()
        #self.my_array.append(data_type)
        
        

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):
            if index >= self.my_logivcal_s or index < -self.my_logivcal_s:
                raise IndexError("Sth wrong eith the index.")
            
            return self.my_array[index]
        
        elif isinstance(index, slice):

            start, stop, step = index.start, index.stop, index.step

            if start is None:
                start = 0
            
            if step is None:
                step = 1

            if - self.my_logivcal_s > start > self.my_logivcal_s or - self.my_logivcal_s >= stop > self.my_logivcal_s:
                raise IndexError("Out of bounds.")
            
            
            array_w_items = self.my_array[:self.my_logivcal_s]

            return array_w_items.tolist()[start:stop:step]
        
        elif type(index) != slice or type(index) != int:
            raise TypeError("Index is not an integer.")

            

        
        #raise NotImplementedError('Indexing not implemented.')
    
    def __setitem__(self, index: int, item: T) -> None:
        if type(index) != int:
            raise TypeError("Index is not an integer.")

        if index <= self.my_logivcal_s - 1:
            #if type(item) != self.d_type:
                #raise TypeError("Wrong type.")
            
            self.my_array[index] = item

        #raise NotImplementedError('Indexing not implemented.')
        """
        start, stop = index.start, index.stop
        
        if start >= self.__logical_size or stop > self.__logical_size or ...:
            raise IndexError("Out of bounds.")
        
        items_to_return = self.__elements[idex]
        """

    def append(self, data: T) -> None:
        if type(data) != self.d_type:
            raise TypeError("Wrong type.")

        if self.my_logivcal_s == self.my_physical_s:
            self.my_physical_s *= 2

            new_array = np.empty(self.my_physical_s)

            for i in range(self.my_logivcal_s):
                new_array[i] = self.my_array[i]
                    
            self.my_array = new_array
        

        self.my_array[self.my_logivcal_s - 1] = data

        self.my_logivcal_s += 1

    def append_front(self, data: T) -> None:
        if type(data) != self.d_type:
            raise TypeError("Wrong type.")

        #resizing array
        if self.my_logivcal_s == self.my_physical_s:
            self.my_physical_s *= 2

            new_array = np.empty(self.my_physical_s)

            for i in range(self.my_logivcal_s):
                new_array[i] = self.my_array[i]
                    
            self.my_array = new_array
        
        for i in range(self.my_logivcal_s,1,-1):
            self.my_array[i] = self.my_array[i-1]
        
        self.my_array[0] = data
        
        #raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        if self.my_logivcal_s >= 1:
            self.my_physical_s -= 1
        
            if self.my_logivcal_s <= 1/4 * self.my_physical_s:
                self.my_physical_s /= 2

                new_array = np.empty(self.my_physical_s)

                for i in range(self.my_logivcal_s):
                    new_array[i] = self.my_array[i]
                
                self.my_array = new_array

        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        del self[0]

        #raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        return self.my_logivcal_s
        raise NotImplementedError('Length not implemented.')

    def __eq__(self, other: object) -> bool:
        for index in range(self.my_logivcal_s):
            if self.my_array[index] != other[index]:
                return False
            
        return True

    def __iter__(self) -> Iterator[T]:
        return self.my_array[:self.my_logivcal_s].flat
        raise NotImplementedError('Iteration not implemented.')

    def __reversed__(self) -> Iterator[T]:
        return self.my_array[self.my_logivcal_s - 1::-1].flat

    def __delitem__(self, index: int) -> None:
        if type(index) != int:
            raise TypeError("Index is not an integer.")
        
        if self.my_logivcal_s < 1/4 * self.my_physical_s:
            self.my_physical_s /= 2

            new_array = np.empty(self.my_physical_s)

            for i in range(self.my_logivcal_s):
                new_array[i] = self.my_array[i]
                
            self.my_array = new_array

        for i in range(index, self.my_logivcal_s-1):
            self.my_array[i] = self.my_array[i+1]

        #raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        
        if item in self.my_array:
            return True
        else:
            return False
        raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        self.my_array = np.array([])
        self.my_logivcal_s = 0
        #raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.my_logivcal_s}, Physical: {self.my_physical_s}, type: {self.d_type}'
    

    def merge(array1, array2):
        new_Array = Array([0 for i in range(len(array1)+len(array2))])
        counter1 = 0
        counter2 = 1
        
        print(type(counter1))

        for i in range(len(array1)):
            new_Array[counter1] = array1[i]
            counter1 += 2

        for y in range(len(array2)):
            new_Array[counter2] = array2[y]
            counter2 += 2

        return new_Array

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')