1) repr method
================================================
The repr() function returns a printable representation of the given object.

class Node():
    def __init__(self, data):
        self.data = data
        self.next  = None

a = Node(3)
print(repr(a))

output: <__main__.Node object at 0x108452460>
  
------------------------------------------------  
  
class Node():
    def __init__(self, data):
        self.data = data
        self.next  = None

    def __repr__(self):
        return "this is the node class of linkedlist"

a = Node(3)
print(repr(a))

output: this is the node class of linkedlist

  
