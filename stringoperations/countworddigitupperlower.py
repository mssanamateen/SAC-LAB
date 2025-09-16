def analyze_sentence(sentence):
    words = len(sentence.split())
    digits = sum(ch.isdigit() for ch in sentence)
    upper = sum(ch.isupper() for ch in sentence)
    lower = sum(ch.islower() for ch in sentence)
    return words, digits, upper, lower


text = input("Enter a sentence: ")
w, d, u, l = analyze_sentence(text)

print("Words:", w)
print("Digits:", d)
print("Uppercase letters:", u)
print("Lowercase letters:", l)
