
class Node:

    def __init__(self, key):

        self.left = None
        self.right = None
        self.key = key

    def inorder(root):
        if root is not None:
            inorder(root.left)
            return (root.key,
            inorder(root.right))
 
 

    def insert(node, key):
    
        if node is None:
            return Node(key)
    
        if key < node.key:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    
        return node
    

 
    def minValueNode(node):
        current = node
    
        while(current.left is not None):
            current = current.left
    
        return current
    

 
    def deleteNode(root, key):
    
        # Base Case
        if root is None:
            return root
    

        if key < root.key:
            root.left = deleteNode(root.left, key)

        elif(key > root.key):
            root.right = deleteNode(root.right, key)

        else:
    
            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    

            temp = minValueNode(root.right)
    

            root.key = temp.key
    
            root.right = deleteNode(root.right, temp.key)
    
        return root
            
# find_val method to compare the value with nodes
    def find_val(self, lkpval):
        if lkpval < self.key:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.find_val(lkpval)
        elif lkpval > self.key:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.find_val(lkpval)
        else:
            print(str(self.key) + ' is found')
   
    
    #find distance
    def pathToNode(root, path, k):
 
        if root is None:
            return False
    
        path.append(root.data)
    
        if root.data == k :
            return True
    

        if ((root.left != None and pathToNode(root.left, path, k)) or
                (root.right!= None and pathToNode(root.right, path, k))):
            return True

        path.pop()
        return False
    
    def distance(root, data1, data2):
        if root:
            path1 = []
            pathToNode(root, path1, data1)

            path2 = []
            pathToNode(root, path2, data2)

            i=0
            while i<len(path1) and i<len(path2):
                if path1[i] != path2[i]:
                    break
                i = i+1
    
            return (len(path1)+len(path2)-2*i)
        else:
            return 0

# Print the tree
    def print_tree(self):
        if self.left:
            self.left.PrintTree()
        print(self.key),
        if self.right:
            self.right.PrintTree()


root = None
for i in range(1_000):
    root = insert(root, i)    
import time
start = time.perf_counter()
root = deleteNode(root, 20)
print(time.perf_counter()-start)

print(root.find_val(7))
print(root.find_val(14))
