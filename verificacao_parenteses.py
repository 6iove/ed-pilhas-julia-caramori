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
    
    def __len__(self):
        return self._size
    
class Verify:
    def __init__(self):
        self.stack = Stack()
        
    def check(self, expression):
        self.stack = Stack()
        
        for character in expression:
            if character == "(":
                self.stack.push("(")
            elif character == ")":
                if len(self.stack) == 0:
                    return "Inválido"
                self.stack.pop()
                
        if len(self.stack) == 0:
            return "Válido"
        else:
            return "Invalid"
        
v = Verify()

test = [
    "((A+B) * C)",
    "(A+B))",
    '((A+B)'
]

for i in test: 
    result = v.check(i)
    print(result)