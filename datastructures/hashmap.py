import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList(Tuple([KT,VT]))] = Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)], data_type=LinkedList)
        self.load_factor_threshold: float = load_factor
        self._count: int = 0
        self._hash_function = custom_hash_function or self._default_hash_function


    def _get_bucket_number(self, key:KT, size) -> int:
        return self._default_hash_function(key) % size

    def __getitem__(self, key: KT) -> VT:
        index = self._get_bucket_number(key, len(self._buckets))
        for ind_key,value in self._buckets[index]:
            if ind_key == key:
                return value
            
        raise KeyError("Item not in list")
            
    
    @staticmethod
    def next_prime(n : int) -> int:

        def is_prime(num:int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
                
            return True
        
        next_prime = n * 2

        while not is_prime(next_prime):
            next_prime += 1
        
        return next_prime

    def _resize(self) -> None:
        new_bucket_size = HashMap.next_prime(len(self._buckets)*2)
        new_bucket: Array[LinkedList[Tuple[KT,VT]]] = Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(new_bucket_size)], data_type= LinkedList)
        for bucket in self._buckets:
            for key, value in bucket:
                new_bucket_number = self._get_bucket_number(key, new_bucket_size)
                new_bucket[new_bucket_number].append((key,value))

        self._buckets = new_bucket

    def __setitem__(self, key: KT, value: VT) -> None:
        if self._count/len(self._buckets) >= self.load_factor_threshold:
            self._resize()

        key_copy = copy.deepcopy(key)
        index = self._get_bucket_number(key, len(self._buckets))
        bucket_chain = self._buckets[index]

        for (k,v) in bucket_chain:
            if k == key_copy:
                bucket_chain.remove((k,v))
                break

        self._buckets[index].append((key_copy,value))
        self._count += 1

        #else:
            #index = self._get_bucket_number(key)
            #self._buckets[index] = value

    def keys(self) -> Iterator[KT]:
        raise
    
    def values(self) -> Iterator[VT]:
        raise NotImplementedError("HashMap.values() is not implemented yet.")

    def items(self) -> Iterator[Tuple[KT, VT]]:
        raise NotImplementedError("HashMap.items() is not implemented yet.")
            
    def __delitem__(self, key: KT) -> None:
        index = self._get_bucket_number(key, len(self._buckets))
        for (k, value) in self._buckets[index]:
            if k == key:    
                self._buckets[index].remove((k, value))
                self._count -= 1
                return
        
        raise KeyError("Item not in list")

        

    def __contains__(self, key: KT) -> bool:
        #1 compute the bucket based on the key
        bucket_index: int = self._get_bucket_number(key, len(self._buckets))

        #2 get the bucket chains in that bucket
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]

        for (k,_) in bucket_chain:
            if k == key:
                return True
            
        return False


    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:

        for bucket in self._buckets:
            for key, _ in bucket:
                yield key


    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap) or len(self) != len(other):
            return False
        
        for key in self:
            if key not in other or self[key] != other[key]:
                return False
        return True


    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)