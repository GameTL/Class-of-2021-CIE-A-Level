#Get a name, then print the ASCII, hex and binary value of each character in a table format
name = input('Enter your name: ')
print('Your name is' + name)
print('+------+-------+-----+---------+')
print('| Code | ASCII | HEX | BINARY |')


for char in name: #For Character in Variable name
    ascii_value = ord(char)
    hex_value = str(hex(ascii_value))
    bin_value = str(bin(ascii_value))
    ascii_value = str(ascii_value)
    print('+------+-------+-----+---------+')
    print('|' + char + '     |' + ascii_value + '    | ' + hex_value[2:] + '   |' + bin_value[2:] + '|')
print('+------+-------+-----+---------+')
