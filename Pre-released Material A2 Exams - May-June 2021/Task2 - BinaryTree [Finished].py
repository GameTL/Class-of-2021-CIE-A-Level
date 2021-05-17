from clearterminal import *
duplicate_flag = False
duplicate_list = []

#_________________________________________________________________________________________________________
class Node():
    def __init__(self, colour, position = None, left_pointer = None, right_pointer = None):
        self.position = position
        self.colour = colour
        self.left_pointer = left_pointer
        self.right_pointer = right_pointer

Maroon = Node('maroon', 0, 1, 2) #0
Black = Node('black', 1, 3, 4) #1
Silver = Node('silver', 2, 5, 6) #2
Amber = Node('amber', 3) #3
Indigo = Node('indigo', 4, 7, 8) #4
Red = Node('red', 5) #5
Violet = Node('violet', 6) #6
Grey = Node('grey', 7 ) #7
Lime_Green = Node('lime green', 8) #8

binarytree = [Maroon, Black, Silver, Amber, Indigo, Red, Violet, Grey, Lime_Green]

#_________________________________________________________________________________________________________

def print_node(Node):
    print('''
Node Position {}
Node Colour: {}
Node Left Pointer: {}
Node Right Pointer: {}'''.format(Node.position, Node.colour, Node.left_pointer, Node.right_pointer))


def asciify(Node, char_position = 0):
    return ord(Node.colour[char_position]) # return int of the first char


def adding_function(Append_Node, Parent_Node = binarytree[0], char_position = 0):
    global duplicate_flag
    if (asciify(Append_Node, char_position)) > (asciify(Parent_Node, char_position)):
        if Parent_Node.right_pointer == None:
            Append_Node.position = len(binarytree)
            Parent_Node.right_pointer = len(binarytree)
            binarytree.append(Append_Node)
        else:
            adding_function(Append_Node, binarytree[Parent_Node.right_pointer], char_position)
    
    elif (asciify(Append_Node, char_position)) < (asciify(Parent_Node, char_position)):
        if Parent_Node.left_pointer == None:
            Append_Node.position = len(binarytree)
            Parent_Node.left_pointer = len(binarytree)
            binarytree.append(Append_Node)
        else:
            adding_function(Append_Node, binarytree[Parent_Node.left_pointer], char_position)
    else:
        if Append_Node.colour == Parent_Node.colour:
            duplicate_flag = True
            duplicate_list.append(Append_Node.colour)
        else:
            adding_function(Append_Node, Parent_Node, char_position +1)


def find_function(Wanted_Node, Parent_Node = binarytree[0], char_position = 0):
    if (asciify(Wanted_Node, char_position)) > (asciify(Parent_Node, char_position)):
        find_function(Wanted_Node, binarytree[Parent_Node.right_pointer], char_position)
    elif (asciify(Wanted_Node, char_position)) < (asciify(Parent_Node, char_position)):
        find_function(Wanted_Node, binarytree[Parent_Node.left_pointer], char_position)
    else: # when they equal
        if Wanted_Node.colour == Parent_Node.colour:
            print("Found at position {} of the list(Starting at 0)".format(Parent_Node.position))
        else:
            find_function(Wanted_Node, Parent_Node, char_position +1)


def print_in_alphabetical_order(Parent_Node = binarytree[0]):
    if ((Parent_Node.left_pointer == None) and (Parent_Node.right_pointer == None)):
        print(Parent_Node.colour)
    if Parent_Node.left_pointer != None:
        print_in_alphabetical_order(binarytree[Parent_Node.left_pointer])
    if Parent_Node.right_pointer != None:
        print_in_alphabetical_order(binarytree[Parent_Node.right_pointer])



def __main__():
    clear()
    Yellow = Node("yellow")
    adding_function(Yellow)

    Yellow = Node("yellow")
    adding_function(Yellow)

    Blue = Node("blue")
    adding_function(Blue)

    for node in binarytree:
        print_node(node)
        print(asciify(node))

    if duplicate_flag:
        print()
        print("all of these colors are already on the list")
        print(duplicate_list)
    
    find_function(Yellow)
    print_in_alphabetical_order()


__main__()
