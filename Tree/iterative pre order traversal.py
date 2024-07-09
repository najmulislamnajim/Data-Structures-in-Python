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
    
    def pre_order_traversal(self): # left root right
        if self.root:
            res=self._pre_order_traversal(self.root)
    
    def _pre_order_traversal(self,root):
        res=[]
        stack=deque()
        stack.append(root)
        while stack:
            temp=stack.pop()
            print(temp.data, end=" ")
            res.append(temp.data)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
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
    tree.pre_order_traversal()
        