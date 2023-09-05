class Stack:
    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) >= self.limit:
            raise Exception("StackOverflow: Stack limit reached.")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            # Since stacks are LIFO, the distance from the top is the reversed index
            distance_from_top = len(self.items) - 1 - self.items.index(target)
            return distance_from_top
        except ValueError:
            # Target not in stack
            return -1
