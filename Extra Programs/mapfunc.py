#map applies function to all items in an iterable
numbers=[1,2,3,4]
squared=list(map(lambda x:x*x,numbers))
print(squared)