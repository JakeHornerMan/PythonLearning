input = "22 (5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))"

class Node(object):
    def __init__(self,id):
        self.id = id
    def __init__(self,statement):
        self.statement = statement

def createExpresion(expression):
    #result = ""
    characters = list(expression)
    number = ""
    counter=0
    increment = 1
    side= ""

    codelines = {}

    for char in expression:
        if char.isnumeric():
            number = number + char
            print(number)
            if counter == 0 and char.next() == " ":
                codelines = "tree = BinaryTree("+ number +")"
                increment += 1
                counter += 1

        elif char == "(":
            number = ""
            print("open")
            if counter == 0:
                codelines = "tree = BinaryTree("+ number +")"
                increment += 1
                counter += 1
            

        elif char == ")":
            number = ""
            print("close")
    
    for key, value in codelines.items():
        print(value[key])
    return codelines

#createExpresion(input)

def createBinTree(expression):
    characters = list(expression)
    print(characters)
    
    codelines = {}
    height = 0
    side = "left"

    number = ""

    for i in range(len(characters)):
        if characters[i].isdigit():
            number = number + characters[i]
            print(number)
            if height == 0 and characters[i+1] == " ":
                codelines = "tree = BinaryTree("+ number +")"
        elif characters[i] == "(":
            height += 1
            number = ""
        elif characters[i] == ")" and characters[i+1] == ")":
            side = "left"

createBinTree(input)