class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False


#Pre-Order Traversal: 
#Checks left path until it ends then goes up by one step checking right node 
#and follows left pathe on this new node path 
#action is then repeated until whole tree is searched
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += "(" + (str(start.value) + ")")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

#In-order Traversal: 
#Left to right traversal in order of most left node
# https://www.techiedelight.com/wp-content/uploads/Inorder-Traversal.png
    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

#Post-Order Traversal:
    def postorder_print(self, start, traversal):
        """Right->Left->Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

#Finf if the tree has a specific 
    def hasPathSum(self, node, sum):
        if node:
            if node.left is None and node.right is None and sum - node.value == 0:
               return True
            else:
                return self.hasPathSum(node.left, sum - node.value) or self.hasPathSum(node.right, sum - node.value)
        else:
            return False

    def pathSumExists(self, node, sum):
        if node is None:
            return False
        if node.value == sum and node.left is None and node.right is None:
            return True    
        return self.pathSumExists(node.left, sum-node.value) or self.pathSumExists(node.right, sum-node.value)
        

#Tree Structure
#1          1
#         /    \
#2       2      3
#      /  \    /  \
#3    4   10   5    8

#Set Root height:1
tree = BinaryTree(1)
#Height:2
tree.root.left = Node(2)
tree.root.right = Node(3)
#Height:3
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(8)

print(tree.print_tree("preorder"))
#(1)(2)(4)(6)(3)(5)(8)
print(tree.print_tree("inorder"))
#4-2-6-1-5-3-8-
print(tree.print_tree("postorder"))

#print(tree.root.value)

#val = input("Enter your value: ")
#val = int(val)

print(tree.pathSumExists(tree.root, 7)) #true
print(tree.pathSumExists(tree.root, 13))
print(tree.pathSumExists(tree.root, 9)) #true
print(tree.pathSumExists(tree.root, 8)) #true
print(tree.pathSumExists(tree.root, 10))
print(tree.pathSumExists(tree.root, 13)) #true