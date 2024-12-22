class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        node = self.head
        i = 0
        while node is not None and i<index:
            node = node.next
            i = i + 1
        if node is None:
            return -1
        return node.data

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head) 
        

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.insertHead(val)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(val)


    def remove(self, index: int) -> bool:
        node = self.head
        prev = None
        i = 0
        while node is not None and i<index:
            prev = node
            node = node.next
            i = i + 1
        if node is None:
            return False
        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next
        return True
        

    def getValues(self) -> List[int]:
        values = []
        node = self.head
        while node is not None:
            values.append(node.data)
            node = node.next
        return values
        
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertHead(1)
    ll.insertTail(2)
    ll.insertTail(3)

    print(ll.getValues())  # [1, 2, 3]

    ll.remove(0)           # Remove the head
    print(ll.getValues())  # [2, 3]

    ll.remove(1)           # Remove the tail
    print(ll.getValues())  # [2]