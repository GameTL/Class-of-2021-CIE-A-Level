list = ["3","4","l"]

with open("test.txt", "a") as file:
    file.write("\n")
    file.writelines(list)

