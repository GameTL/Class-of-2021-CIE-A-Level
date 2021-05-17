def check_ISBN_valid(number):
    if len(number) != 13:
        print('invalid')
    else:
        # Get given check digit
        given_check_digit = int(number[12])
        number1s = int(number[0])+int(number[2])+int(number[4])+int(number[6])+int(number[8])+int(number[10])
        number2s = (int(number[1])+int(number[3])+int(number[5])+int(number[7])+int(number[9])+int(number[11]))*3
        sum_of_products = number1s + number2s
        print(sum_of_products)
        remainder = sum_of_products % 10
        if remainder == given_check_digit:
            print("It's valid")
        else:
            print("It's invaild")1


# Welcome the user
print('This program checks an ISBN number is valid')
number = input('Enter an ISBN number: ')

# Formatting the number
number = number.replace('-', '')
number = number.replace(' ', '')
# Perform check digit calculation

check_ISBN_valid(number)