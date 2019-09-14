class LinkedList:
    '''Linked-List of nodes of primative data types'''
    def __init__(self, head=None):
        self.head = head
    
    def getHead(self):
        return self.head

    # Big O(1) - Inserts new Node at index(0) and shifts data down
    def insert(self, data):
        '''Inserts data node at the beginning of the linked-list'''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Big O(n) - Must goes to nth elem to add to end
    def push(self, data):
        ''' \'Pushes\' data to the end of the linked list'''
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            curr = self.head
            while(curr.next is not None):
                curr = curr.next
            curr.next = new_node
    
    # Big O(n) - Must go to (n-1)th elem
    def pop(self):
        '''Removes data node at the end of the linked-list'''
        if self.head == None:
            print("Linked-List is empty!!!")
        elif self.head.next == None:
            self.head = None
        else:
            prev = self.head
            curr = self.head.next
            while(curr.next is not None):
                prev = curr
                curr = curr.next
            prev.next = None

    # Big O(n) - Worst case is last elem n
    def get(self, index):
        '''Gets data element at index'''
        curr = self.head
        for i in range(1, index):
            curr = curr.next
        return curr.data
    
    def __str__(self):
        string = "LinkedList: ["
        if self.head is not None:
            string+=f"{self.head.data}"
            curr = self.head.next
            while(curr is not None):
                string+=f",{curr.data}"
                curr = curr.next
        string+="]"
        return string

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def getData(self):
        return self.data