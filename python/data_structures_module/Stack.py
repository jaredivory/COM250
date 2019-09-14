class Stack:
    '''LIFO Implementation'''
    
    def __init__(self, data=[]):
        self.data = data

    def pop(self):
        self.data.pop()
    
    def push(self, data):
        self.data.insert(0, data)

    def __str__(self):
        string = f"Stack: [{self.data[0]}"
        for val in self.data[1:]: 
            string+= f", {val}"
        return string + "]"