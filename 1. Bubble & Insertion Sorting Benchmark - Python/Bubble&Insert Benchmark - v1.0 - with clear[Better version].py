# By GameTL
# os.system('cls') for Windows
# os.system('clear') for Unix
import random
import time
import os
import platform
platform = platform.system()
if platform == 'Darwin':
    clear = "clear"
elif platform == 'Windows':
    clear = 'cls'

# generate a random list

def generate_list():
    global mylist
    print("How many numbers would you like to generate and sort? (integers only)")
    n = int(input())
    print()
    print("Enter the minimum and maximum of the randomly generated numbers")
    range_min = int(input("Min: "))
    range_max = int(input("Max: "))
    mylist = []
    for i in range(n):
        random_int = random.randint(range_min, range_max)
        mylist.append(random_int)


def bubble_sort():
    global bubble_list
    bubble_list = mylist
    n = len(bubble_list)
    for i in range(n):
        for index in range(n-1):
            if bubble_list[index] > bubble_list[index+1]:
                bubble_list[index], bubble_list[index+1] = bubble_list[index+1], bubble_list[index]
    

def insert_sort():
    global insert_list
    insert_list = mylist
    for index in range(1, len(insert_list)):
        current_value = insert_list[index]
        current_position = index
        while current_position > 0 and insert_list[current_position - 1] > current_value:
            insert_list[current_position] = insert_list[current_position - 1]
            current_position = current_position - 1
            insert_list[current_position] = current_value


os.system(clear)
generate_list()
start_time_bubble = time.time_ns()
bubble_sort()
finish_time_bubble = time.time_ns()
start_time_insert = time.time_ns()
insert_sort()
finish_time_insert = time.time_ns()
time_taken_bubble = (finish_time_bubble - start_time_bubble)
time_taken_insert = (finish_time_insert - start_time_insert)
time_difference = time_taken_bubble/time_taken_insert
os.system(clear)
print('''



''')
print("Randomly genrerated list")
print(mylist)
print('''------------------------------------------------------------
''')
print('''Bubble list sorted
''')
print(bubble_list)
print("Bubble sorting time: " + str(time_taken_bubble) + "ns")
print('''
------------------------------------------------------------''')
print('''Insert list sorted
''')
print(insert_list)
print("Insert sorting time: " + str(time_taken_insert) + "ns")
print('''
------------------------------------------------------------''')
print("Insert is " + str(int(time_difference)) + "x faster than bubble sorting")
print()
