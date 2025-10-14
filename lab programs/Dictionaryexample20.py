student = {
    "name": "Amulya",
    "rollno": 103,
    "course": "CSE(AI)-B"
}

print("Dictionary items:")
'''.items() returns all the key–value pairs in the dictionary.'''
for key, value in student.items():
    print(key, ":", value)
