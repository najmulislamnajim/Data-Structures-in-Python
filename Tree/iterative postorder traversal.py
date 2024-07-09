from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        queue=deque()
        newnode=TreeNode(data)
        if self.root is None:
            self.root = newnode
            return
        queue.append(self.root)
        while queue:
            temp=queue.popleft()
            if temp.left is not None:
                queue.append(temp.left)
            else:
                temp.left = newnode
                newnode.parent = temp
                return

            if temp.right is not None:
                queue.append(temp.right)
            else:
                temp.right = newnode
                newnode.parent = temp
                return
    
    def post_order_traversal(self): # left right root
        res=[]
        stack=deque()
        cur=self.root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                temp=stack[-1].right
                if temp:
                    cur=temp
                else:
                    temp=stack.pop()
                    res.append(temp.data)
                    print(temp.data, end=" ")
                    while stack and temp==stack[-1].right:
                        temp=stack.pop()
                        res.append(temp.data)
                        print(temp.data, end=" ")
                    
                    
    
    def postorder_traversal_using_two_stacks(self):
        res=[]
        stack1=deque()
        stack2=deque()
        stack1.append(self.root)
        while stack1:
            temp=stack1.pop()
            stack2.append(temp)
            if temp.left:
                stack1.append(temp.left)
            if temp.right:
                stack1.append(temp.right)
        while stack2:
            temp=stack2.pop()
            print(temp.data , end=" ")
            res.append(temp.data)
        return res

    def postorder_travarsal(self):
        res=[]
        stack1=deque()
        stack1.append(self.root)
        while stack1:
            temp=stack1.pop()
            res.append(temp.data)
            if temp.left:
                stack1.append(temp.left)
            if temp.right:
                stack1.append(temp.right)
        res=res[::-1]
        return res
            
            

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(60)
    tree.insert(70)
    tree.postorder_traversal_using_two_stacks()
    print()
    tree.post_order_traversal()
    print()
    res=tree.postorder_travarsal()
    print(res)
        