student1 = {'Name': 'Game', 'Age': 18, 'Subject': 'CS'}
print(student1)

student1['phone'] = '555-555-555'
print(student1)

student1.update({'Name': 'Tinapat'})
student1.get('Name')
print(student1)

del student1['Age']
print(student1)
print(student1.keys())
print(student1.values())
print(student1.items())
