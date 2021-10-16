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

    def print_tree(self):
        return self.preorder_print(tree.root, "")

#Pre-Order Traversal: 
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += "(" + (str(start.value) + ")")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


    #Sum of all branches
    def sum(self,root,total_sum,sum_list):
        if root is None:
            return
        total_sum += root.value
        self.sum(root.right,total_sum,sum_list)
        self.sum(root.left,total_sum,sum_list)
        if root.left is None and root.right is None:
            sum_list.append(total_sum)


#1          10
#         /    \
#2       2      7 
#      /  \    /  \
#3    4    6  5    8
tree = BinaryTree(10)
tree.root.left = Node(2)
tree.root.right = Node(7)
tree.root.left.left = Node(4)
tree.root.left.right = Node(6)
tree.root.right.left = Node(5)
tree.root.right.right = Node(8)

print(tree.print_tree())

var = input("Text: ")
target = int(var)
sum_list = []
tree.sum(tree.root,0,sum_list)
print(sum_list)
#target = 7
if target in sum_list:
    print("YES")
else:
    print("NO")