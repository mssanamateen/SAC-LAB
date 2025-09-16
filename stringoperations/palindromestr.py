def palindrome(*names):
    for name in names:
        if name==name[::-1]:
            print(f"{name} is plaindrome")
        else:
            print(f"{name} is not a palindrome")

if __name__=="__main__":
    palindrome("mom","madam","run")
    
