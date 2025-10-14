class_info = {
    "class_name": "CSE(AI)",
    "semester": 3,
    "subject": "SAC LAB"
}

students = [
    {"name": "reda naz", "roll_no": 85},
    {"name": "Grecia", "roll_no": 90},
    {"name": "Amulya", "roll_no": 103}
]

def display_class_info():
    print("Class Information:")
    for key, value in class_info.items():
        print(f"{key.capitalize()} : {value}")

def display_students():
    print("\nStudents List:")
    for s in students:
        print(f"Roll No: {s['roll_no']} - Name: {s['name']}")
