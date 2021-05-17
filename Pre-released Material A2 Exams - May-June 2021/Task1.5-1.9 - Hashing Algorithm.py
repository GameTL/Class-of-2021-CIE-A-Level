MOD_NUMBER = 20 # the algorithm

# Task 1.6
def write_hashing_algorithms(book_string):
    book_id = book_string[0:3]
    hashed_id = int(book_id) % MOD_NUMBER # Task 1.5 Hashing Algorithm
    while hash_table[hashed_id] != "":
        hashed_id = hashed_id + 1
    hash_table[hashed_id] = book_string # Task 1.8

# Task 1.9
def read_hashing_algorithms(book_string):
    book_id = book_string[0:3]
    hashed_id = int(book_id) % MOD_NUMBER
    while (hash_table[hashed_id])[0:3] != book_id:
        hashed_id = hashed_id + 1
    print(hash_table[hashed_id])



# Creating MOD_NUMBER length array
hash_table = []
for i in range(MOD_NUMBER):
    hash_table.append("")

with open("BookCollection.txt", "r") as file:
    book_list = file.readlines()
    for book in book_list:
        write_hashing_algorithms(book)

print()
print(hash_table)

search1 = input("Find: ")
read_hashing_algorithms(search1)
search1 = input("Find: ")
read_hashing_algorithms(search1)


