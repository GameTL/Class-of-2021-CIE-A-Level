dividend = int(input_denary)
remainders = []
input_denary = int(input("enter your denary number to be converted pls"))

while True:
    remainder = dividend % 2
    quotient = dividend // 2
    remainders.append(remainder)
    if quotient == 0:
        break
    dividend = quotient
remainder.reverse()
print(remainder)

