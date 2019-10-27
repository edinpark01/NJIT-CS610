class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, passenger):
        self.queue.append(passenger)
    
    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return self.queue.__len__() == 0
    
    def size(self):
        return len(self.queue)