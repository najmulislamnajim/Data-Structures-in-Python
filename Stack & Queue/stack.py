#Stack using List

class StackUsingList:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        for data in self.stack:
            print(data, end=' ')
        print()
            
if __name__ == '__main__':
    stack=StackUsingList()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.display()
    print(stack.size())
    print(stack.is_empty())
    stack.pop()
    stack.display()
    print(stack.peek())
    stack.display()
    print(stack.pop())
    stack.display()
    print(stack.size())
    
# Stack using collection.deque
from collections import deque

class StackUsingDeque:
    def __init__(self):
        self.stack = deque()
    
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        for data in self.stack:
            print(data, end=' ')
        print()
        
if __name__ == '__main__':
    stack=StackUsingDeque()
    stack.push(2)
    stack.push(4)
    stack.push(6)
    stack.push(8)
    stack.display()
    print(stack.size())
    print(stack.is_empty())
    stack.pop()
    stack.display()
    print(stack.peek())
    stack.display()
    print(stack.pop())
    stack.display()
    print(stack.size())
        
# Stack using Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.top = None
        self.sz = 0
        
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode
        self.sz += 1
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_data = self.top.data
            self.top = self.top.next
            self.sz -= 1
            return popped_data
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data
        
    def is_empty(self):
        return self.sz == 0
    
    def size(self):
        return self.sz
    
    def display(self):
        current = self.top
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
        
if __name__ == '__main__':
    stack=StackUsingLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()
    print(stack.size())
    print(stack.is_empty())
    stack.pop()
    stack.display()
    print(stack.peek())
    stack.display()
    print(stack.pop())
    stack.display()
    print(stack.size())