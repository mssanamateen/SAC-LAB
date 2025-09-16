def count_vcb(s):
    vowels="aeiouAEIOU"
    v=c=b=0
    for ch in s:
        if ch in vowels:
            v+=1
        elif ch.isalpha():
            c+=1
        elif ch.isspace():
            b+=1
    return v,c,b

text=input("enter a string:")
v,c,b=count_vcb(text)
print(f"vowels: {v}, Consonants:{c}, blanks:{b}")
