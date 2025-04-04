from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T
DEBUG1 = False
class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.
        
            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''
        self._maxsize = maxsize
        self.rear = 0
        self._front = 0
        self.count = 0
        self.data_type = data_type

        self.queue = Array([data_type()]* maxsize,data_type)
        #raise NotImplementedError

    def __getitem__(self,index):
        return self.queue[index]
    
    def __contains__(self, item):
        return item in self.queue
        
    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')
            
            Arguments:
                item: The item to add to the queue
                
            Raises:
                IndexError: If the queue is full
        '''
        
        if self.count == self.maxsize:
            raise IndexError("List is full")
        
        self.queue[self.rear] = item
        if self.rear == 5:
            self.rear = 0
        self.rear += 1
        self.count += 1
        DEBUG1 and print("enqueue:",self.queue)

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2
                >>> q.dequeue()
                3
                >>> q.dequeue()
                IndexError('Queue is empty')
                >>> q.dequeue()
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''

        removed_item = self.queue[self._front]
        self.queue[self._front] = 0
        if self._front == self._maxsize:
            self._front = 0
        self._front += 1
        self.count -= 1
        DEBUG1 and print("dequeue:",self.queue)
        return removed_item
    
        #raise NotImplementedError

    def clear(self) -> None:
        ''' Removes all items from the queue '''
        raise NotImplementedError
    
    def front_index(self):
        return int(self._front)

    def rear_index(self):
        return int(self.rear)
    
    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        if self._front == self.rear:
            raise IndexError("The queue is empty")
        DEBUG1 and print("front:",self.queue[self._front], "front nbr:", self._front)
        DEBUG1 and print("rear:", self.rear)
        DEBUG1 and print(self.queue)
        return self.queue[self._front]

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise 
        
            Returns:
                True if the queue is full, False otherwise
        '''
        if self.count == self._maxsize:
            return True

        else: 
            return False
    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise
        
            Returns:
                True if the queue is empty, False otherwise
        '''
        if self._front == self.rear and self.count == 0:
            return True
        
        else:
            return False
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue
        
            Returns:
                The maximum size of the queue
        '''
        return self._maxsize

    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise
        
            Equality is defined as:
                - The front and rear pointers are equal
                - The elements between the front and rear pointers are equal, even if they are in different positions
                
            Arguments:
                other: The object to compare this CircularQueue to
                
            Returns:
                True if this CircularQueue is equal to another object, False otherwise
        '''

        """
        checklist = []
        checklist_other = []
        
        for i in range(self.count):
            self_index = (self.front_index() + i) % self.maxsize
            other_index = (other.front_index() + i) % other.maxsize

            print(other_index, other.rear_index())
            print(self_index)
            
            checklist.append(self.queue[self_index])
            x = other.front_index() + other_index
            if x == other._maxsize:
                x = 0
            checklist_other.append(other[x])
            

        print(checklist)
        print(checklist_other)

        for i in range(len(checklist)):
            if checklist[i] in checklist_other:
                checklist_other.pop(checklist_other.index(checklist[i]))

        
        if len(checklist_other) == 0:
            return True

        else: 
            return False
            
        """
        checklist = []
        checklist_other = []
        
        for i in range(self.count):
            self_index = (self._front + i) % self.maxsize
            other_index = (other._front + i) % other.maxsize
            
            checklist.append(self.queue[self_index])
            checklist_other.append(other[other_index])

            print(checklist, "\n", checklist_other)
            if self.queue[self_index] != other.queue[other_index]:
                return False

            

        return True
        
        

    
    def __len__(self) -> int:
        ''' Returns the number of items in the queue
        
            Returns:
                The number of items in the queue
        '''
        return self.count

    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue
        
            Returns:
                A string representation of the queue
        '''
        return str(self.queue)

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object
        
            Returns:
                A string representation of the CircularQueue object
        '''
        return f'ArrayQueue({repr(self.circularqueue)})'