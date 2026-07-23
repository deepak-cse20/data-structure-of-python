class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(f"{item}is pushed")
    def pop(self):
        if self.is_empty():
            return "stack underflow"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "stack is Empty"
        return self.stack [-1]
    def is_empty(self):
        return len(self.stack[-1])
    def is_empty(self):
        return len(self.stack)==0
    def size (self):
        return len (self.stack)
    def display (self):
        print("stack elements:",self.stack)
s=stack()
s.push(19)
s.push(55)        
s.push(23)
s.push(33)
s.pop()
s.peek()
s.size()
s.display()
print("top element :",s.peek())