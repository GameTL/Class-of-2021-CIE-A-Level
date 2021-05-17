````````````````listified_letters = []
print('Enter your text for bruteforce')
encrypted_text = input()
increment = 1
# chr(65) = A,(chr or character)  ord('12') = A,  (ord = ordinal )
for i in range(24):
    for letter in encrypted_text:
        ascii_letters = ord(letter)
        raw_incremented = int(ascii_letters) + int(increment)
        if raw_incremented == 32:
            incremented = raw_incremented
            return_letter = chr(incremented)
        elif raw_incremented > 122: # for +increment
            incremented = raw_incremented - 26
            return_letter = chr(incremented)
        else:
            incremented = raw_incremented
            return_letter = chr(incremented)
        listified_letters.append(return_letter)
    print('This is your encrypted message: ' + ''.join(listified_letters))
    listified_letters = []
    increment = increment + 1
