#Binary Search Tree
class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
        
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key == data:
            return
        if self.key > data :
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data) 
    def search(self, data):
        if self.key == data : #If root node is equal to given data
            print("Node is found")
            return
        
        if self.key > data :
            if self.lchild is None: #There is No Node in left side
                print("Node is not found")
            else:
                self.lchild.search(data)
                
        else:
            if self.rchild: #If there is node in right side
                self.rchild.search(data)
            else:
                print("Node is not found")
                
    def preorder(self): # Root node ---> Left node ---> Right node.
        print(self.key, end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def postorder(self): # Left node ---> Right node ---> Root node
        if self.lchild:
             self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end = ' ')
    def inorder(self): # Left node --->Root node ---> Right node 
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end = " ")
        if self.rchild:
            self.rchild.inorder()
    def delete(self,data):
        if self.key is None:
            print("Tree is empty")
            return
        if self.key > data:
            if self.lchild:
                self.lchild= self.lchild.delete(data)
            else:
                print("Tree is empty")
        elif self.key < data:
            if self.rchild:
                self.rchild= self.rchild.delete(data)
            else:
                print("Tree is empty")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self

    def min(self):
        current = self
        while current.lchild:
             current = current.lchild
        print("Node with smallest key: ",current.key)
    def max(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Node with Largest key: ",current.key)
# def count(node):
#     if node is None:
#         return 0
#     return 1+count(node.lchild)+count(node.rchild)
    

                
            
        
        
            
            

root = BST(100)

for i in range(26):
    root.insert(i)

# print(count(root))
print("Pre-Order")
root.preorder()
print()

# root.min()
# # root.max()
# root.preorder()
print("In order")
root.inorder()
print()
# print("post-Order")
# root.postorder()
    
                
            
            
            
            
        