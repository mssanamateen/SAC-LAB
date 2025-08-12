print(2 + 3 * 4)   # 3*4=12 → 2+12=14

print((2 + 3) * 4)  # (2+3)=5 → 5*4=20

print(2 + 3 ** 2)   # 3**2=9 → 2+9=11

print(-3 * 2)  # -3 * 2 = -6

print(2 ** 3 ** 2)  # 3**2=9 → 2**9=512

print(100 / 5 * 2 % 6)  # 100/5=20.0 → 20.0*2=40.0 → 40.0%6=4.0

print(3 < 5 < 10)   # True because 3<5 and 5<10
print(3 < 5 > 2)    # True because 3<5 and 5>2

print(2 + 3 << 2)   # 2+3=5 → 5<<2 = 20

print(3 < 5 and 10 > 2)   # True and True → True
print(3 < 5 or 10 < 2)    # True or False → True

print(not True or False)      # (not True)=False → False or False → False
print(not (True or False))    # True or False = True → not True = False

a = b = c = 5
print(a, b, c)  # 5 5 5
print(5 & 3 + 2)  # 3+2=5 → 5 & 5 = 5

print(-2 ** 2)   # -(2**2) = -4
print((-2) ** 2) # (-2)**2 = 4

print(2 + 3 * 4 ** 2 / 8)  
# 4**2=16 → 3*16=48 → 48/8=6.0 → 2+6.0=8.0

print(2 & 3 == 2)  # 2&3=2 → 2==2 → True

print(True + True * False)  # 1 + 1*0 = 1
