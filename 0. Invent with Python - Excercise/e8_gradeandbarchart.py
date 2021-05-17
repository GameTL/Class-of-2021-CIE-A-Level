# Get a list of stuident grades and then print as a bar chart
grades = []
number_of_grades = int(input('How many grades you want to enter?'))
# i is for counting loop
for i in range(number_of_grades):
    grade = input('input a grade')
    grades.append(grade)
# grade is a value & 
for grade in grades:
    print('|' * int(grade) + '  ' + grade)
