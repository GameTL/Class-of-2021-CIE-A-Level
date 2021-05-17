# Write s Caesar Cypher to encrypt & decrypt
# 1. input a text

# 2. Select a letters to a list.
listified_letters = ()
print('Enter your text for encryption')
text = input()
increment = input("Set an increment(i.e.4,-5): ")
# chr(65) = A,(chr or character)  ord('12') = A,  (ord = ordinal )
for letter in text:
    ascii_letters = ord(letter)
    raw_incremented = int(ascii_letters) + int(increment)
    if raw_incremented > 122: # for +increment
        incremented = raw_incremented - 26
        return_letter = chr(incremented)
    elif raw_incremented == 32:
        incremented = ascii_letters + int(increment)
        return_letter = chr(incremented)
    elif raw_incremented < 97: # for -increment
        incremented = raw_incremented + 26
        return_letter = chr(incremented)
    else:
        incremented = raw_incremented
        return_letter = chr(incremented)
    listified_letters.append(return_letter)
print('This is your encrypted message: ' + listified_letters)
