# logic
# F(1) = 0
# F(2) = 1
# F(n) = F(n-1)+ F(n-2)
# therefore  f(n-1) = F(n-2)+ F(n-3)
import os
import time
import platform
platform = platform.system()
if platform == 'Darwin':
	clear = "clear"
elif platform == 'Windows':
	clear = 'cls'


def fibbonacci(m):
	n = int(m)
	if n <= 2:
		return n
	else:
		return_number = int(fibbonacci(n-1)) + int(fibbonacci(n-2))

		return return_number


def run_main():
	global n, number_of_n
	os.system(clear)
	print("Find number for the nth term in the Fibbonacci ")
	n = float(input(""))
	n = n - 1
	if n <= 0 or n % 1 != 0:  
		print("Sorry, nth term has to be a positive integers")
		print()
		run_main()
	else:
		number_of_n = (fibbonacci(n))
		print(number_of_n)


run_main()
os.system(clear)
print("""
The value of term {} is {}

""".format(str(int(n+1)), str(int(number_of_n))))
time.sleep(1.5)