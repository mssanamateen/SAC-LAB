# Function to perform optional string operations using keyword arguments
def string_tools(text, strip=False, replace_space=False, find_word=None, starts_with=None, ends_with=None):
    if strip:
        text = text.strip()   # remove spaces at start & end
    if replace_space:
        text = text.replace(" ", "_")  # replace spaces with underscores
    if find_word:
        return f"'{find_word}' found at index {text.find(find_word)}"
    if starts_with:
        return text.startswith(starts_with)
    if ends_with:
        return text.endswith(ends_with)
    return text
print(string_tools("   hello world   ", strip=True))       
print(string_tools("hello world", replace_space=True))     
print(string_tools("hello world", find_word="world"))      
print(string_tools("hello world", starts_with="he"))       
print(string_tools("hello world", ends_with="ld"))         
