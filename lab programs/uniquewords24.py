# Print all unique words from a text file in alphabetical order

filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        text = file.read()

    # Split into words and remove punctuation
    words = text.split()
    clean_words = [word.strip('.,!?()[]{}":;') for word in words]

    # Use a set to find unique words
    unique_words = sorted(set(clean_words), key=str.lower)

    print("\nUnique words in alphabetical order:")
    for word in unique_words:
        print(word)

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
