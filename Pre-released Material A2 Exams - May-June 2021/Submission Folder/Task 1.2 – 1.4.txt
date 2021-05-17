# Task 1.2
def enter_code():
    global book_code
    book_code = input("Book unique code: ")
    if (int(book_code) < 100) or (int(book_code) > 999):
        print("invalid")
        enter_code() 
def enter_title():
    global book_title
    book_title = input("Title of the book: ") 

def enter_author():
    global book_author
    book_author = input("Main author: ") 

def enter_year():
    global book_year
    book_year = input("Year of Publication: ")
    if (int(book_code) <= 0 and int(book_code) >= 9999):
        print("invalid")
        enter_year() 

# Task 1.3
with open("BookCollection.txt", "a") as file: 
    array = [] 
    for i in range(10): # its 10 in the exams
        print("This is for book #" + str(i+1))
        print("format example: 101_Harry Potter_JK_1997")
        enter_code()
        enter_title()
        enter_author()
        enter_year()
        book = book_code + "_ " + book_title + "_" + book_author + "_" + book_year + "\n" 
        array.append(book) 
        print(book + "is stored") 
    file.writelines(array) 


# Task 1.4
with open("BookCollection.txt", "r") as file:
    booklist = file.readlines()
    i = 1 
    print(booklist)
    for book in booklist:
        current_book = book.split("_")
        print("This is book number " + str(i))
        print("Book code: " + current_book[0])
        print("Book name: " + current_book[1])
        print("Book author: " + current_book[2])
        print("Book year of publication: " + current_book[3])
        i = i + 1 
