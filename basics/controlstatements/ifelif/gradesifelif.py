score=float(input("enter your score"))
if score <0 or score >1:
    print("Wrong input")
elif score >=0.9:
    print("Your Grade is A")
elif score >=0.8:
    print("Your Grade is B")
elif score >=0.7:
    print("Your Grade is C")
elif score >=0.6:
    print("Your Grade is D")
else:
    print("Your Grade is F")
