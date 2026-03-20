class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def push(self, data):
            new_node = Node(data)       
            new_node.next = self.head   
            self.head = new_node        
            self._size = self._size + 1
            
    def pop(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        self._size = self._size - 1
        return removed.data
    
    def print_stack(self):
        new_node = self.head
        while new_node:
            print(new_node.data)
            new_node = new_node.next
            
    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    
    def __len__(self):
        return self._size 
    
s = Stack()

s.push("O")
s.push("M")
s.push("T")
s.push("I")
s.push("R")
s.push("O")
s.push("G")
s.push("L")
s.push("A")

s.print_stack()

while len(s) > 0:
    s.pop()
    
print(s.peek())