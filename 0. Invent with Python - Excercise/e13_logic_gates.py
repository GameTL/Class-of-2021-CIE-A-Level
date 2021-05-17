# NOT
def not_gate(a):
    input('Enter your 1st bit: ')
    if a == '0':
        return '1'
    else:
        return '0'
# AND
def and_gate(a, b):
    if a == '0' or b == '0':
        return '0'
    else:
        return '1'
# OR
def or_gate(a, b):
    if a == '1' or b == '1':
        return '1'
    else:
        return '
        
        
        
        '
# NAND
def nand_gate(a, b):
    if a == '0' or b == '0':
        return '0'
    else:
        return '1'
# NOR
def nor_gate(a, b):
    if a == '0' or b == '0':
        return '1'
    else:
        return '0'
# XOR
def xor_gate(a, b):
    if a == b:
        return '0'
    else:
        return '1'
#  This is a Logic Gate calculator
print('''Choose your function:
1: NOT Gate
2: AND Gate
3: OR Gate
4: NAND Gate
5: NOR Gate
6: XOR Gate''')
chosen_func = input()

if chosen_func == '1':
    a = input('Enter your 1st bit: ')
    print(a, ' is ', not_gate(a))
else:
    a = input('Enter your 1st bit: ')
    b = input('Enter your 2nd bit: ')
    if chosen_func == '2':
        print(a + ' AND ' + b + ' is ' + and_gate(a, b))
    elif chosen_func == '3':
        print(a + ' OR ' + b + ' is ' + or_gate(a, b))
    elif chosen_func == '4':
        print(a + ' NAND ' + b + ' is ' + nand_gate(a,b))
    elif chosen_func == '5':
        print(a + ' NOR ' + b + ' is ' + nor_gate(a,b))
    elif chosen_func == '6':
        print(a + ' XOR ' + b + ' is ' + xor_gate(a,b))
