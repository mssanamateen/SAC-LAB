# Function to optionally perform string operations
def string_operations(text, perform_operations=True):
    if perform_operations:
        return text.upper(), text.lower(), text.title()
    else:
        return text  # Just return the string as it is

print(string_operations("hello world"))                
print(string_operations("hello world", False))        
