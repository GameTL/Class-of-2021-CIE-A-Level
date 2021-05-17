import time
from collections import deque
import os
import platform
platform = platform.system()
if platform == 'Darwin':
    clear = "clear"
elif platform == 'Windows':
    clear = 'cls'


def time_pause():
    time.sleep(0.5)



def check_if_queue_is_empty():
    if queue:
        empty = False
    else:
        empty = True
        os.system(clear)
        print("Your queue is empty")
        input("""
Press enter to choose a function""")
        which_function()
    # empty

def run_fetch():
    check_if_queue_is_empty()
    os.system(clear)
    print(queue.popleft())
    continue_flag = input("""

type / to fetch the next element
    
Press enter to choose a function
""")
    if continue_flag == "/":
        run_fetch()
    else:
        which_function()


def run_add():
    string_to_incut = input("""What to append to the list?
    
    """)
    queue.append(string_to_incut)
    which_function()


def run_add_priority():
    string_to_incut = input("""What to append to the list?
    
    """)
    queue.appendleft(string_to_incut)
    which_function()





def which_function():
    os.system(clear)
    fetch_or_add_or_priority = input(str("""Would you like to 'add' or 'fetch' element to the queue?
"addp" for priority queue

default list is """ + str(queue) + """
["add" or "fetch" or "addp"]
"""))
    if fetch_or_add_or_priority == "fetch":
        run_fetch()
    elif fetch_or_add_or_priority == "add":
        run_add()
    elif fetch_or_add_or_priority == "addp":
        run_add_priority()
    else:
        os.system(clear)
        print('["add" or "fetch"]')
        which_function()
global queue
queue = deque(['Data 1', 'Data 2', 'Data 3'])

which_function()