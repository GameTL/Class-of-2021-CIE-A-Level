import random
class Tools: # Task 3.2
    def __init__(self, name, cost, image_file_name):
        self.name = name # string
        self.cost = cost # reals
        self.image_file_name = image_file_name # string 

class Shelves:
    def __init__(self, array):
        self.position = random.randint(0,4) # only 0-4
        self.array = array 

# Task 3.4
def add_tool_to_shelf(tool, shelf):
    if len(shelf.array) < 10:
        shelf.array.append(tool)
    else:
        print("shelf is full, max 10 tools") 

def read_tool_from_shelf(shelf):
    for i in range(len(shelf.array)):
        current_tool = Shelf1.array(i)
        print(i)
        print(current_tool) 

# Task 3.5
def list_item_in_self(shelf):
    i = 1
    for tool in shelf.array:
        print("Tool number {0}".format(i))
        print("Tool: {}".format(tool.name))
        print("Cost: ${}".format(tool.cost)) 
        print()
        i += 1 

Object1 = Tools("Hammer", "100", "hammer.jpg")
Object2 = Tools("Premium Hammer", "200", "hammer.jpg") 

BASE_ARRAY = []
Shelf1 = Shelves(BASE_ARRAY) 
add_tool_to_shelf(Object1, Shelf1)
add_tool_to_shelf(Object2, Shelf1)
add_tool_to_shelf(Object1, Shelf1)
add_tool_to_shelf(Object2, Shelf1)
add_tool_to_shelf(Object1, Shelf1)
add_tool_to_shelf(Object2, Shelf1)
add_tool_to_shelf(Object1, Shelf1)
add_tool_to_shelf(Object2, Shelf1)
add_tool_to_shelf(Object1, Shelf1)
add_tool_to_shelf(Object2, Shelf1) # 10th
add_tool_to_shelf(Object1, Shelf1) # 11th 
input("Tool added, enter to list all item")
list_item_in_self(Shelf1) 
