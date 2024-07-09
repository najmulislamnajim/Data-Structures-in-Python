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
    
    def traverse(self):
        stack=deque()
        preorder=[]
        postorder=[]
        inorder=[]
        if self.root is None:
            return
        stack.append([self.root,1])
        while stack:
            top=stack.pop()
            if top[1]==1:
                preorder.append(top[0].data)
                stack.append([top[0],2])
                if top[0].left:
                    stack.append([top[0].left,1])
                    
            elif top[1]==2:
                inorder.append(top[0].data)
                stack.append([top[0],3])
                if top[0].right:
                    stack.append([top[0].right,1])
            else:
                postorder.append(top[0].data)
        
        result=[preorder,inorder,postorder]
        return result
            

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(60)
    tree.insert(70)
    res=tree.traverse()
    print(res)
        