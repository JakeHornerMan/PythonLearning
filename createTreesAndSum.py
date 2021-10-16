class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

def createNodeList(node_list):
    number = ""
    for char in input:
        if char.isnumeric():
            number = number + char
        else:
            node_list.append(number)
            number = ""

    node_list = [i for i in node_list if i != '']
    node_list = [int(i) for i in node_list]
    return node_list
    

def createBinaryTree(self,node_list):
    if len(node_list) ==0:
        return None

    current = node_list[0]
    rightChildIndex = len(node_list)

    for idx, value in enumerate(node_list):
        if value > current:
            rightChildIndex = idx
            break

    leftChildTree = self.createBinaryTree(node_list[1:rightChildIndex])
    rightChildTree = self.createBinaryTree(node_list[rightChildIndex:])
    return BinaryTree(current, leftChildTree, rightChildTree)

#def create(node_list):

def sum(self,root,total_sum,sum_list):
    if root is None:
        return
    total_sum += root.value
    self.sum(root.right,total_sum,sum_list)
    self.sum(root.left,total_sum,sum_list)
    if root.left is None and root.right is None:
        sum_list.append(total_sum)
    return sum_list



input = "22 (5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))"

node_list = []
goal= 0

node_list = createNodeList(node_list)

goal = node_list[0]
node_list.pop(0)
    
print(goal)
print(node_list)

tree = createBinaryTree(node_list)

print(tree)

sum_list = []
sum(tree.root,0,sum_list)
print(sum_list)

if goal in sum_list:
    print("YES")
else:
    print("NO")