class Node:
    def __init__(self,value):
        self.data=value
        self.prev=None
        self.next=None
        
class doublyLinkedList(Node):
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def insertAtHead(self,data):
        self.length+=1
        newnode=Node(data)
        if self.head is not None:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
        else:
            self.head=newnode
            self.tail=newnode
    
    def insertAtTail(self,value):
        self.length+=1
        newnode=Node(value)
        if self.tail is not None:
            self.tail.next=newnode
            newnode.prev=self.tail 
            self.tail=newnode
        else:
            self.tail=newnode
            self.head=newnode
            
    def traverseFromHead(self):
        if self.head is not None:
            node=self.head
            while node:
                print(node.data, end=' ')
                node=node.next  
            print()
            
    def traverseFromTail(self):
        if self.tail is not None:
            node=self.tail
            while node:
                print(node.data, end=' ')
                node=node.prev
            print()
    
    def insertAt(self,value,index):
        if index>self.length:
            return None 
        if index==0:
            self.insertAtHead(value)
        elif index==self.length:
            self.insertAtTail(value)
        else:
            if self.head is not None:
                self.length+=1
                newnode=Node(value)
                currentNode=self.head 
                for i in range(index):
                    currentNode=currentNode.next
                temp=currentNode.prev
                temp.next=newnode
                newnode.prev=temp
                currentNode.prev=newnode
                newnode.next=currentNode
    
    def deleteFromHead(self):
        if self.length==1:
            self.head=None
            self.tail=None
            self.length=0
        else:
            self.head=self.head.next
            self.head.prev=None
            self.length-=1
            
    def deleteFromTail(self):
        if self.length==1:
            self.head=None
            self.tail=None
            self.length=0
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            self.length-=1
          
    def deleteAt(self,index):
        if index>=self.length:
            return None
        else:
            if index==0:
                self.deleteFromHead()
            elif index==self.length-1:
                self.deleteFromTail()
            else:
                self.length-=1
                current=self.head
                for i in range(index):
                    current=current.next 
                current.prev.next=current.next
                current.next.prev=current.prev
                  
    def size(self):
        return self.length
     
    def sortTest(self):
        count=0
        while True:
            count+=1
            mark=0
            node=self.head
            while node:
                if node.next and node.data>node.next.data:
                    temp=node.data
                    node.data=node.next.data
                    node.next.data=temp
                    mark+=1
                node=node.next
            if mark==0:
                break
        print('total count is ',count)
            
        
if __name__ == '__main__':
    list=doublyLinkedList()
    list.insertAtHead(8)
    list.insertAtHead(6)
    list.insertAtHead(4)
    list.insertAtHead(2)
    list.traverseFromHead()
    list.traverseFromTail()
    print(list.size())
    list.insertAtTail(10)
    list.traverseFromHead()
    list.traverseFromTail()
    print(list.size())
    list.insertAt(0,0)
    list.traverseFromHead()
    print(list.size())
    list.insertAt(12,6)
    list.traverseFromHead()
    print(list.size())
    list.insertAt(5,3)
    list.traverseFromHead()
    print(list.size())
    list.deleteFromHead()
    list.deleteFromTail()
    list.traverseFromHead()
    list.traverseFromTail()
    print(list.size())
    list.deleteAt(2)
    list.traverseFromHead()
    print(list.size())
    
    mylist=doublyLinkedList()
    mylist.insertAtHead(59)
    mylist.insertAtHead(37)
    mylist.insertAtHead(92)
    mylist.insertAtHead(39)
    mylist.insertAtHead(19)
    mylist.insertAtHead(73)
    mylist.insertAtHead(57)
    mylist.traverseFromHead()
    mylist.sortTest()
    mylist.traverseFromHead()