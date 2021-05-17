binaryTree = []

class TreeNode:
    def __init__ (self, value, nextNodeL=None, nextNodeR=None, parentNode=None):
        self.value = value
        self.nextNodeL = nextNodeL
        self.nextNodeR = nextNodeR

def CreateRoot(value):
    root = TreeNode(value)
    binaryTree.append(root)

def AttachLeft(NodeData, ParentNode):
    binaryTree[ParentNode].nextNodeL = TreeNode(NodeData)
    binaryTree.append(TreeNode(NodeData))

def AttachRight(NodeData, ParentNode):
    binaryTree[ParentNode].nextNodeR = TreeNode(NodeData)
    binaryTree.append(TreeNode(NodeData))


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
for node in binaryTree:
    print(node.value)
