# build a binary search tree
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
# assuming no replicates in the tree 
class BSTree(object):
    def __init__(self):
        self.root=None
    
    def isEmpty(self):
        return self.root==None
    
    def printTree(self): # in order traverse, recursion
        def printNode(root):
            if root==None:
                return
            printNode(root.left)
            print(root.val)
            printNode(root.right)
            return
        printNode(self.root)
    
    def insert(self, val):
        if self.isEmpty():
            self.root=Node(val)
            return
        current=self.root
        while current!=None:
            if current.val==val:
                return None # replicates error
            elif current.val>val:
                prev=current
                current=current.left
            else:
                prev=current
                current=current.right
        if prev.val>val:
            prev.left=Node(val)
            return prev.left
        else:
            prev.right=Node(val)
            return prev.right
    
    def search(self, target): # recursive search
        def searchNode(root):
            if root==None: return None
            if root.val==target: return root
            if root.val>target: return searchNode(root.left)
            else: return searchNode(root.right)
        return searchNode(self.root)
    
    def delete(self, target): # iterative search
        if self.root==None: return False #Failed deletion
        current=self.root
        if current.val==target:
            self.root=None
            del current
            return True
        while current!=None:
            
    
    def destroyTree(self):
        raise NotImplementedError

# Testing
myList=[3,1,4,1,5,9,2,6,5,5]
print("Initializing the tree ...")
myTree=BSTree()
for i in myList:
    print(f'Was {i} inserted? {myTree.insert(i)}')

print("In order traverse the tree ...")
myTree.printTree()

print("Search existing number ...")
print(myTree.search(4))

print("Search non-existing number ...")
print(myTree.search(10))

