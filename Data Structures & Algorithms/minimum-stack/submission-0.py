class MinStack:

    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def push(self, val: int) -> None:
        self.first_stack.append(val)

        if len(self.second_stack) == 0:
            self.second_stack.append(val)
        else:
            min_val = self.second_stack[-1]
            if val <= min_val:
                # the pushed val is smaller than min_val
                self.second_stack.append(val)
            else:
                self.second_stack.append(min_val)

    def pop(self) -> None:
        val = self.first_stack.pop()
        min_val = self.second_stack.pop()

    def top(self) -> int:
        return self.first_stack[-1]

    def getMin(self) -> int:
        return self.second_stack[-1]
