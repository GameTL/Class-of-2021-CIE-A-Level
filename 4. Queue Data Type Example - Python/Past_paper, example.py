# 9608 42 s18   https://paper.sc/doc/5b80ea0b06bb3922177454b0/
BinaryTree = []


class TreeNode:
    def __init__(self, value, nextNodeL="-1", nextNodeR="-1"):
        self.value = value
        self.nextNodeL = nextNodeL
        self.nextNodeR = nextNodeR


def CreateRoot(value):
    root = TreeNode(value)
    BinaryTree.append(root)


def AttachLeft(NodeData, ParentNode):
    BinaryTree[ParentNode].nextNodeL = TreeNode(NodeData)
    BinaryTree.append(TreeNode(NodeData))


def AttachRight(NodeData, ParentNode):
    BinaryTree[ParentNode].nextNodeR = TreeNode(NodeData)
    BinaryTree.append(TreeNode(NodeData))


def TraversingBinaryTree(CurrentNode):
    global BinaryTree
    if ((BinaryTree[CurrentNode].RightPointer.value == "-1") and (BinaryTree[CurrentNode].LeftPointer.value == "-1")):
        print(BinaryTree[CurrentNode].DataValue)
    if BinaryTree[CurrentNode].LeftPointer != "-1":
        TraversingBinaryTree(BinaryTree[CurrentNode].LeftPointer)
    if BinaryTree[CurrentNode].RightPointer != "-1":
        TraversingBinaryTree(BinaryTree[CurrentNode].RightPointer)
    return


CreateRoot("Red")
AttachLeft("Blue", 0)
AttachRight("Green", 0)
AttachRight("Black", 2)
AttachLeft("Brown", 2)
AttachLeft("Peach", 3)
AttachLeft("Yellow", 1)
AttachRight("Purple", 1)
AttachLeft("White", 6)
AttachLeft("Pink", 7)
AttachLeft("Grey", 9)
AttachRight("Orange", 9)
print(BinaryTree)
TraversingBinaryTree(BinaryTree[0])


'''
for node in BinaryTree:
    print(node.value)
'''




