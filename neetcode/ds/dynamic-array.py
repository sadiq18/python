"""

Design Dynamic Array (Resizable Array)
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.

Example 1:

Input:
["Array", 1, "getSize", "getCapacity"]

Output:
[null, 0, 1]
Example 2:

Input:
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

Output:
[null, null, 1, null, 2]
Example 3:

Input:
["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

Output:
[null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
Note:

The index i provided to get(int i) and set(int i) is guaranteed to be greater than or equal to 0 and less than the number of elements in the array.


"""



class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__index__ = 0
        self.__data__ = [None for i in range(capacity)]

    def get(self, i: int) -> int:
        return self.__data__[i]


    def set(self, i: int, n: int) -> None:
        self.__data__[i] = n


    def pushback(self, n: int) -> None:
        if self.__index__ == self.capacity:
            self.resize()
        self.__data__[self.__index__] = n
        self.__index__ = self.__index__ + 1


    def popback(self) -> int:
        num = self.__data__[self.__index__-1]
        self.__index__ = self.__index__ - 1
        return num
 

    def resize(self) -> None:
        for i in range(self.capacity):
            self.__data__.append(None)
        self.capacity = len(self.__data__)
        


    def getSize(self) -> int:
        return self.__index__
        
    
    def getCapacity(self) -> int:
        return len(self.__data__)
    


if __name__ == "__main__":
    """
    ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
    """
    arr = DynamicArray(1) # [None]
    print(arr.getSize()) # 0
    print(arr.getCapacity())  # 1
    print(arr.pushback(1)) # [1]
    print(arr.getSize()) #1 
    print(arr.getCapacity()) #1 
    print(arr.pushback(2)) # [1,2]
    print(arr.getSize()) # 2
    print(arr.getCapacity()) #2 
    print(arr.get(1)) # 2
    print(arr.set(1,3)) # [1,3]
    print(arr.get(1)) # 3
    print(arr.popback()) 
    print(arr.getSize())
    print(arr.getCapacity())








