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
                return False # replicates error
            elif current.val>val:
                prev=current
                current=current.left
            else:
                prev=current
                current=current.right
        if prev.val>val:
            prev.left=Node(val)
            return True
        else:
            prev.right=Node(val)
            return True
    def search(self, val):
        raise NotImplementedError
    def delete(self, val):
        raise NotImplementedError
    def destroyTree(self):
        raise NotImplementedError

myList=[3,1,4,1,5,9,2,6,5,5]
myTree=BSTree()
for i in myList:
    print(f'Was {i} inserted? {myTree.insert(i)}')
print("In order traverse the tree ...")
myTree.printTree()
