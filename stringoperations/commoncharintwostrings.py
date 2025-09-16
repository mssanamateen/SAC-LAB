def common_char(str1,str2):
    for char in str1:
        if char in str2:
            print(f" character {char} is found in both strings")

common_char('rose','pose')
