# Collatz recursion
import math
import os
import platform
import time
platform = platform.system()
if platform == 'Darwin':
	clear = "clear"
elif platform == 'Windows':
	clear = 'cls'

def operator(n):
    if n == 1:
        return 1
    elif n%2 == 0: # therefore even number
        n = operator(n/2)
        counter +=1
    elif n%2 == 1:
        n = operator((3*n) + 1)
        counter +=1
    
    print(int(n))





n = int(input("Number to be put into a recursion function: "))
counter = 0
os.system(clear)
operator(n)


    

print()
print("n is now 1, it took " + str(counter) + " time")
time.sleep(1)