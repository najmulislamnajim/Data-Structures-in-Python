class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0
    
    def InsertAtHead(self,data):
        newnode = Node(data)
        newnode.next=self.head
        self.head = newnode
        self.length+=1
    
    def InsertAtTail(self,data):
        newnode = Node(data)
        if not self.head:
            self.head=newnode
            self.length+=1
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        self.length+=1
        
    def Traverse(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()
    def ListSize(self):
        print(f'List size is : {self.length}')
            
myList = LinkedList()
myList.InsertAtHead(5)
myList.InsertAtHead(7)
myList.InsertAtHead(9)
myList.Traverse()
myList.ListSize()
myList.InsertAtTail(3)
myList.InsertAtTail(1)
myList.Traverse()
myList.ListSize()