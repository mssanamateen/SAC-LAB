# Multiplication table using for + while + break

for num in range(1, 4):       # displays table for 1,2,3
    print(f"\nTable of {num}:")
    
    mul = 1
    while mul <= 10:          # inner loop → multipliers 1 to 10
        if mul == 5:          # stop table early when mul = 5
            break
        print(f"{num} x {mul} = {num * mul}")
        mul += 1
