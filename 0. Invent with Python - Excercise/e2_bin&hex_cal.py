denary = int(input("Input the number in Denary:")) 
binary = ""
while denary>0:
    binary = str(denary%2) + binary
    denary = denary//2
print("Your binary Number:" + binary)
