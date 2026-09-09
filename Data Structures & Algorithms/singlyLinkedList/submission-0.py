class LinkedList:
    
    def __init__(self):
        self.arr = []
    
    def get(self, index: int) -> int:
        if index >= len(self.arr):
            return -1
        return self.arr[index]

    def insertHead(self, val: int) -> None:
        newArr = [val]
        for x in self.arr:
            newArr.append(x)
        self.arr = newArr

    def insertTail(self, val: int) -> None:
        self.arr.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.arr):
            return False
        newArr = []
        for i in range(len(self.arr)):
            if i != index:
                newArr.append(self.arr[i])
        self.arr = newArr
        return True

    def getValues(self) -> List[int]:
        return self.arr
