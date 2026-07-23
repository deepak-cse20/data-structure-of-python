class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def is_empty(self):
        return self.top is None
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        print(f"{value} is pushed")
    def pop(self):
        if self.is_empty():
            return None
        popped_data=self.top.value
        self.top=self.top.next
        return popped_data
    def peek(self):
        if self.is_empty():
            return None
        return self.top.value
stack=Stack()
stack.push(1)
stack.push(6)
stack.push(3)
print("peek:",stack.peek())
print("pop:",stack.pop())

