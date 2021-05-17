my_keypad = ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']
print('This is your keypad')
for row in my_keypad:  # take row ['1', '2', '3'] from keypad
    keypad_row = ''
    for column in row: 
        column = column + ' '
        keypad_row += column  # add column to keypad_row
    print(keypad_row)

