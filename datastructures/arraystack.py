import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''

        
        self.data_type = data_type
        self.max_size = max_size
        self.stack = Array([data_type]*max_size)

        #variables
        self.top_index = -1
        self.count = 0
        
        


        #raise NotImplementedError('ArrayStack is not implemented')

    def push(self, item: T) -> None:
        #raise NotImplementedError
        self.stack[self.count] = item
        self.count += 1
        self.top_index += 1
        if self.count > self.max_size:
            raise IndexError("Stack is already full")

    def pop(self) -> T:
        #raise NotImplementedError
        if self.count == 0:
            raise IndexError("Stack is empty")
        x = self.top_index
        self.top_index -= 1
        self.count -= 1
        self.stack.pop()
        return self.stack[x]

    def clear(self) -> None:
       self.stack.clear()
       self.count = 0
       self.top_index = -1

    def count_num(self):
        return self.count
    
    @property
    def peek(self) -> T:
       return self.stack[self.top_index]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self.max_size
    
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        if self.count == self.maxsize:
            return True
        else:
            return False
        
    @property
    def empty(self) -> bool:
        return self.count == 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrayStack):  
            return False 

        if self.count_num() != other.count_num():  
            return False  
        
        
        for i in range(self.count):
            if self.stack[i] != other.stack[i]:
                return False 

        return True

    def __len__(self) -> int:
        return self.count
    
    def __contains__(self, item: T) -> bool:
       return item in self.stack

    def __str__(self) -> str:
        return str([self.stack[i] for i in range(self.count)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

