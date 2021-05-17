# Get list of number, output the odd & number into a list
print('')
print('')
list_number = []
odd_number = []
even_number = []
print('This a code that sort even and odd numbers')
print('How many number you want to input?')
numbers_in_list = int(input('Numbers: '))

print('')
print('')


# i is for counting loop.   list_number.append is adding number from input into list_number
for i in range(numbers_in_list):
    number = input('Input number for sorting: ')
    list_number.append(number) # put the new input into the list append(at the back)

print(list_number)
for number in list_number: # for every number in the list, if the remainder is 1 it's odd
    remainder = int(number) % 2
    if remainder == 1:
        odd_number.append(number)
    else:
        even_number.append(number)

print('')
print('The odd numbers are')
print(', '.join(odd_number))
print('')
print('The even numbers are')
print(', '.join(even_number))
print('')
print('')
print(', '.join(even_number))
# .join is to join all the numbers in the list and ',' is to seperate the numbers




