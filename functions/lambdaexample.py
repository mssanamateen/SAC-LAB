''' A lambda function is a small
anonymous function defined using lambda keyword. 
It can take any number of arguments but can only have one 
expression'''

#lambda arguments: expression


square=lambda x:x*2
print(square(5))


add=lambda x,y:x+y
print(add(3,4))

greet=lambda: "hello"
print(greet())

multiply=lambda x,y:x*y
print(multiply(3,4))

names=['sana','mateen']
'''map() returns an object which is an iterator thats why
it is passed to list() for conversion to list'''
upper_names=list(map(lambda x:x.upper(), names))
print(upper_names)