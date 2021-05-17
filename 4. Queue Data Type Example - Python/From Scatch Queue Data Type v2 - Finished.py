import time
import os
import platform
platform = platform.system()
if platform == 'Darwin':
	clear = "clear"
elif platform == 'Windows':
	clear = 'cls'

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Queue:
	
	def __init__(self):  # initialise queue
		self.front = self.rear = None  # both front and rear of the queue is set to null

	def isEmpty(self):
		return self.front == None  # check if front of the queue is empty
	
	# Method to add an item to the queue
	def EnQueue(self, item): 
		temp = Node(item)  
		
		if self.rear == None:  # for no existing queue
			self.front = self.rear = temp
			return
		self.rear.next = temp
		self.rear = temp

	# Method to remove an item from queue 
	def DeQueue(self):
		
		if self.isEmpty():
			return
		temp = self.front
		self.front = temp.next
		if(self.front == None):
			self.rear = None



def time_pause():
	time.sleep(0.5)


def run_enqueue():
	os.system(clear)
	string_to_enqueue = str(input("""What to enqueue to the list? """))
	q.EnQueue(string_to_enqueue)
	listing_queues()
	continue_flag = input("""
type / to continue enqueue
Press enter to choose a function
""")
	if continue_flag == "/":
		run_enqueue()
	else:
		enqueue_or_dequeue_function()


def run_dequeue():
	os.system(clear)
	if q.isEmpty() == False:
		print("Dequeued: " + str(q.front.data))
		q.DeQueue()
		
		continue_flag = input("""

type / to fetch the next element

Press enter to choose a function
""")
		if continue_flag == "/":
			run_dequeue()
		else:
			enqueue_or_dequeue_function()
		
	else:
		print("Your queue is empty")
		enqueue_or_dequeue_function()
		


def listing_queues():
	my_q_list = []
	# while q.rear.next !== None:
	inital_front = q.front
	while q.isEmpty() == False:
		my_q_list.append(str(q.front.data))
		temp = q.front
		q.front = temp.next
	print(my_q_list)
	q.front = inital_front


def enqueue_or_dequeue_function():
	os.system(clear)
	listing_queues()
	print()
	print("Queue Front: " + str(q.front.data))
	print("Queue Rear: " + str(q.rear.data))
	print()
	enqueue_or_dequeue = input(str("""Would you like to enqueue 'e' or dequeue 'd' element to the queue?
'exit' for breaking out
"""))
	if enqueue_or_dequeue == "e":
		os.system(clear)
		run_enqueue()
	elif enqueue_or_dequeue == "d":
		os.system(clear)
		run_dequeue()
	elif enqueue_or_dequeue == "exit":
		return
	else:
		os.system(clear)
		print('["enqueue" or "dequeue"]')
		enqueue_or_dequeue_function()




# Driver Code
if __name__ == '__main__':
	q = Queue()
	q.EnQueue("51")
	q.EnQueue("52")
	q.EnQueue("53")
	q.EnQueue("54")
	enqueue_or_dequeue_function()
	
