greeting="Hello"
def string_operations():
	name="Alice"
	full_greeting=greeting+","+name+"!"
	print(full_greeting)
	substring1=full_greeting[0:5]
	print("Substring 1",substring1)
	substring2=full_greeting[7:]
	print("Substring 2",substring2)
	char_at_6=full_greeting[6]
	print(f"character at index6 is{char_at_6}")
string_operations()
