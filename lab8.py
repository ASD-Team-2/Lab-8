class Node:

    def __init__(self, key):

        self.left = None
        self.right = None
        self.key = key
            
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
            a=1
            #print(str(self.key) + ' is found')
   
# Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        #print(self.key),
        if self.right:
            self.right.print_tree()
 
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
 
    return current
 
 
 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
 
#
def insert(node, key):
 
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    # return the (unchanged) node pointer
    return node
 

def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root
 
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        return root
      
     
    if root.left is None and root.right is None:
          return None
 
 
    if root.left is None:
        temp = root.right
        root = None
        return temp
 
    elif root.right is None:
        temp = root.left
        root = None
        return temp
 
 
    succParent = root
 
 
    succ = root.right
 
    while succ.left != None:
        succParent = succ
        succ = succ.left
 

    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
 
    # Copy Successor Data to root
 
    root.key = succ.key
 
    return root

#find distance
def pathToNode(root, path, k):
 
    if root is None:
        return False
 
    path.append(root.key)
    if root.key == k :
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


def creating_ht(n):

    root = None
    for i in range(n):
        root = insert(root, i)    
    return root

def benchmark():
    from timeit import default_timer as timer

    for i in range(0, 2):
        n=(10**(i+3))
	
        ht = creating_ht(n)
        start = timer()
        ht=insert(ht, 500)
        end = timer()
        print("Insertion time: {} sec".format(end-start) + " of {} nums.".format(n))

        start = timer()
        ht = deleteNode(ht, 20)
        end = timer()
        print("Removing time: {} sec".format(end-start) + " of {} nums.".format(n))

        start = timer()
        ht.find_val(7)
        end = timer()
        print("Searcing time: {} sec".format(end-start) + " of {} nums.".format(n))

        start = timer()
        dist = distance(ht, n/3, 2*n/3)
        end = timer()
        print("Find distance time: {} sec".format(end-start) + " of {} nums.".format(n))

        start = timer()
        ht.print_tree()
        end = timer()
        print("Graph traversal time: {} sec".format(end-start) + " of {} nums.".format(n))

        start = timer()
        a  = minValueNode(ht)    
        end = timer()
        print("Find min time: {} sec".format(end-start) + " of {} nums.".format(n))

if __name__=="__main__":
    import sys
    sys.setrecursionlimit(10**9)
    benchmark()
 
