import numpy as np
Array = np.array
from datastructures.array import Array
"""
def main():
    
    print("Hello, World!")

    x = {}
    x["name"] = "Diedrik"
    print(x)
    print(x["name"])
    print(x.values)

if __name__ == '__main__':
    main()
"""
"""
data = [1,2,3,4]
print(type(data))
#for index in range(len(data)):
#    data[index] = -99

for item in data:
    item = 99
"""
"""
data = Array("hello", str(0))
liste = [num for num in range(10)]


print(data)
#print(data[0])
"""
"""
lister = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list1 = []
for row in lister:
    print(row)
    list1.append(list(row))

print(list1)
"""

"""
data = ["hello", "danke", "hallo"]
data.pop("hello")
print(data)
"""



"""
array1 = Array([5,7,17,13,11])
array2 = Array([12,10,2,4,6])

new_array = Array.merge(array1,array2)
print(new_array)

class Women():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.age}"
    
    def __str__(self):
        return f"Halt die Fresse"
    
clara = Women("clara", 30)

print(repr(clara))
"""


print("hallo",3,"\n","Hallo")