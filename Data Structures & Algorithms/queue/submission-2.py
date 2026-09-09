class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def isEmpty(self) -> bool:
        return (self.length == 0)

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.next = first_node
        first_node.prev = new_node
        new_node.prev = self.head

        self.length +=1


    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        new_node.next = self.tail
        last_node.next = new_node
        new_node.prev = last_node
        self.tail.prev = new_node

        self.length +=1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            last_node = self.tail.prev
            self.tail = last_node
            self.length -=1
            return last_node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            first_node = self.head.next
            self.head = first_node
            self.length -=1
            return first_node.val
