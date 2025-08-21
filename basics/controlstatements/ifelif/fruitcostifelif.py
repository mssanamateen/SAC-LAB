fruit_type = input("Enter the Fruit Type: ").strip().title()
'''.strip().title() on input to make input case-insensitive and trim spaces'''
if fruit_type == "Oranges":
    print('Oranges are ₹50 per kilogram')
elif fruit_type == "Apples":
    print('Apples are ₹120 per kilogram')
elif fruit_type == "Bananas":
    print('Bananas are ₹40 per dozen')
elif fruit_type == "Cherries":
    print('Cherries are ₹600 per kilogram')
else:
    print(f'Sorry, we are out of {fruit_type}')
