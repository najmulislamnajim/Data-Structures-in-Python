#queue using list

class QueueusingList:
    def __init__(self):
        self.queue = []
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def front(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]
    def display(self):
        for data in self.queue:
            print(data, end=' ')
        print()
        
if __name__ == '__main__':
    queue = QueueusingList()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(7)
    queue.display()
    print('Front:', queue.front())
    print('Dequeue:', queue.dequeue())
    queue.display()
    print('Size:', queue.size())
    print('Is empty?', queue.is_empty())
    queue.enqueue(9)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.display()
    print('Size:', queue.size())
    print('Is empty?', queue.is_empty())
    
# Queue usning deque

from collections import deque

class QueueUsingDeque:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def front(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]
    def display(self):
        for data in self.queue:
            print(data, end=' ')
        print()
        
if __name__ == '__main__':
    queue = QueueUsingDeque()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(8)
    queue.display()
    print('Front:', queue.front())
    print('Dequeue:', queue.dequeue())
    queue.display()
    print('Size:', queue.size())
    print('Is empty?', queue.is_empty())
    queue.enqueue(10)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.display()
    print('Size:', queue.size())
    print('Is empty?', queue.is_empty())
    
# Queue using LinkedList

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class QueueUsingLinkedList:
    def __init__(self):
        self.frnt = None
        self.rear = None
        self.sz = 0
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.frnt = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.sz += 1
    
    def dequeue(self):
        if self.frnt is None:
            return None
        data = self.frnt.data
        self.frnt = self.frnt.next
        if self.frnt is None:
            self.rear = None
        self.sz-=1
        return data
    
    def front(self):
        if self.frnt is None:
            return None
        data=self.frnt.data
        return data
    
    def is_empty(self):
        return self.sz == 0
    
    def size(self):
        return self.sz
    
    def display(self):
        current = self.frnt
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
        
if __name__ == '__main__':
    queue = QueueUsingLinkedList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.display()
    print('Front:', queue.front())
    print('Dequeue:', queue.dequeue())
    queue.display()
    print('Size:', queue.size())
    print('Is empty?', queue.is_empty())
    queue.enqueue(5)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.display()
    print('Size:', queue.size())
    print('Is empty?', queue.is_empty())
