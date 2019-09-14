class Queue:
    '''FIFO'''

    def __init__(self, size):
        self.size = size
        self.nElems = self.end = 0
        self.front = 0
        self.queue = [None] * size
    
    def isEmpty(self):
        return self.size != self.nElems
    
    def isFull(self):
        return self.size == self.nElems
    
    def getSize(self):
        return self.size

    # TODO: Fix EnQueue and DeQueue!!!
    def enQueue(self, elem):
        if self.isFull():
            print("Queue is Full!")
            return
        self.queue[self.nElems - self.front] = elem
        self.nElems += 1
    

    def deQueue(self):
        print(self.nElems)
        elem = self.queue[self.nElems]
        self.queue[self.nElems] = None
        self.nElems -= 1
        return elem

    def __str__(self):
        string = "Queue: "
        string += str(self.queue)
        return string