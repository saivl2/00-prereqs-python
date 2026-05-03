students = ['Hermione', 'Harry', 'Ron', 'Draco']

for i in range(len(students)):
    print(i, students[i])

students = {
    'Hermione': 'Gryffindor',
    'Harry': 'Gryffindor',
    'Ron': 'Gryffindor',
    'Draco': "Slytherin"
}

print(students['Ron'])

for student in students: # displays keys by default
    print(student, students[student])