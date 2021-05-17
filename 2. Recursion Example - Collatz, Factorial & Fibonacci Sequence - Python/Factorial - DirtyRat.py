import os
import platform
platform = platform.system()
if platform == 'Darwin':
	clear = "clear"
elif platform == 'Windows':
	clear = 'cls'


def factorial(m):
	n = int(m)
	if n == 1:
		return 1
	else:
		return_number = int(n) * int(factorial(n-1))
		print(str(n) + "! = " + str(return_number))
		return return_number
		

def run_main():
	print("Input number to calculate the factorial the number")
	n = float(input(""))
	os.system(clear)
	if n <= 0 or n % 1 != 0:  
		print("Sorry, factorial only works for positive integers")
		print()
		run_main()
	else:
		factorial(n)



run_main()