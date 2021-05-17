import os
import platform
platform = platform.system()
if platform == 'Darwin':
    clear = "clear"
elif platform == 'Windows':
    clear = 'cls'



class Node:  #  60% from geeksforgeeks/binary-search-tree-set-1-search-and-insertion
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def append_to_tree(root, input_data):
    if root is None:
        return Node(input_data)
    else:
        if root.value == input_data:
            return root.value
        elif root.value < input_data:
            root.right = append_to_tree(root.right, input_data)
        else:
            root.left = append_to_tree(root.left, input_data)
    return root


# from scratch

def ask_to_find_in_tree(root):
    print("Which number would you like to find in the tree?")
    to_find = int(input())
    find_in_tree(root, to_find)


def find_in_tree(root, input_data):
    if root is None:
        return Node(input_data)
    else:
        if root.value == input_data:  # check root is input_data
            print("Found " + str(root.value))
            return root.value
        elif root.value > input_data:  # check left of root
            if root.left is None:
                print("Not in the list")
                return Node(input_data)
            else:
                return find_in_tree(root.left, input_data)
        else:                         # check right of root
            if root.right is None:
                print("Not in the list")
                return Node(input_data)
            else:
                return find_in_tree(root.right, input_data)

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


def append_to_list(root, my_list): 
    if root: 
        # First print the data of node
        my_list.append(root.value)
        # Then recur on left child 
        append_to_list(root.left, my_list) 
        # Finally recur on right child 
        append_to_list(root.right, my_list)
    

def insertion_sorting(my_list):
    for index in range(1, len(my_list)):
        current_value = my_list[index]
        current_position = index
        while current_position > 0 and my_list[current_position - 1] > current_value:
            my_list[current_position] = my_list[current_position - 1]
            current_position = current_position - 1
            my_list[current_position] = current_value


def print_tree_as_list(root):
    my_list = []
    append_to_list(root, my_list)
    insertion_sorting(my_list)
    print(my_list)


# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


def what_to_do(root):
    os.system(clear)
    print_tree_as_list(root)
    print("""'a' for appending to tree
'f' to find a number in a tree
    """)
    to_do = input()
    if to_do == "a":
        os.system(clear)
        print_tree_as_list(root)
        print("what do you want to append to the tree?")
        input_data = int(input())
        append_to_tree(root, input_data)
        input("Enter to continue")
        what_to_do(root)
    elif to_do == "f":
        os.system(clear)
        print_tree_as_list(root)
        ask_to_find_in_tree(root)
        input("Enter to continue")
        what_to_do(root)


# r1 default .value = 50

os.system(clear)
r1 = Node(50)
r1 = append_to_tree(r1, 20)
r1 = append_to_tree(r1, 25)
r1 = append_to_tree(r1, 10)
r1 = append_to_tree(r1, 100)
r1 = append_to_tree(r1, 70)
what_to_do(r1)

