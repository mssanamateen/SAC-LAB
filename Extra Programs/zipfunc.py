#zip combines iterables
names=['Alice','Riya','Siya']
ages=[20,30,40]
for name,age in zip(names,ages):
    print(f"{name} is {age}")