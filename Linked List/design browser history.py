class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        self.currentPosition=0
        self.currentNode=None
    
    def insert(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
        self.size+=1
        self.currentNode=newNode
        self.currentPosition+=1
        
    def back(self,step):
        possibleSlot=self.currentPosition-1
        if not possibleSlot:
            return self.currentNode.value
        if possibleSlot<step:
            step=possibleSlot
        return self._backHelper(step)
    
    def _backHelper(self,step):
        node=self.currentNode
        while step:
            node=node.prev
            step-=1
            self.currentPosition-=1
        self.currentNode=node
        return self.currentNode.value
    
    def forward(self,step):
        possibleSlot=self.size-self.currentPosition
        if not possibleSlot:
            # print("if block")
            return self.currentNode.value
        if possibleSlot<step:
            step=possibleSlot
        return self._forwardHelper(step)
    
    def _forwardHelper(self,step):
        node=self.currentNode
        while step:
            node=node.next
            step-=1
            self.currentPosition+=1
        self.currentNode=node
        return self.currentNode.value
    
    def visit(self,url):
        node=self.currentNode
        self.size=self.currentPosition
        node.next=None
        self.tail=node
        self.insert(url)
        
class BrowserHistory:
    def __init__(self,url):
        self.list=DoublyLinkedList()
        self.homePage=url
        self.list.insert(url)
    
    def visit(self,url):
        self.list.visit(url)
    
    def back(self,steps):
        return self.list.back(steps)
    
    def forward(self,steps):
        return self.list.forward(steps)
    
        

if __name__=='__main__':
    browserHistory=BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    print(browserHistory.back(1))
    print(browserHistory.back(1))
    print(browserHistory.forward(1))
    browserHistory.visit("linkedin.com")
    print(browserHistory.forward(2))
    print(browserHistory.back(2))
    print(browserHistory.back(7))
    