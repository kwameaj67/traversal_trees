class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self,root): 
        self.root = Node(root) #assigning root of tree
     
    def print_tree(self,type): #prints tree
        if type == "preorder":
            return self.preorder(tree.root,"")
        else:
            print("traversal type" + str(type) + "is not supported")
            return False
     
        #start is the string that updates on every traversal func
        #traversal prints on every recursive call
        # roots > left > right
    def preorder(self,start,traversal):
        if start: #if node isn't null
            traversal += (str(start.value) + ",") #print value and concat it to traversal string
            
            traversal = self.preorder(start.left,traversal)
            traversal = self.preorder(start.right,traversal)
        return traversal
             
           

#setup tree
tree = BinaryTree(10)
tree.root.left = Node(5)
tree.root.right = Node(40)
tree.root.left.left = Node(1)
tree.root.left.right = Node(7)
tree.root.right.right = Node(50)

# print(tree.print_tree("preorder"))
print(tree.preorder(tree.root,""))
