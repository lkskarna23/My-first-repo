#14. **Score Grader:** Prompt for a score between 0.0 and 1.0.
#Print `A` ($\ge 0.9$), `B` ($\ge 0.8$), `C` ($\ge 0.7$), `D` ($\ge 0.6$), or `F` ($< 0.6$). Print an error message if out of range.


score=float(input("enter score between 0.0 to 1.0 : "))
if 0<score<1:
    if score>=0.9:
        print(f"{score} Grade is A ")
    elif score>=0.8:
        print(f"{score} Grade is B")
    elif score>= 0.7:
        print(f"{score} Grade is C")
    elif score>= 0.6:
        print(f"{score} Grade is D")
    elif score<0.6:
        print(f"{score} Grade is F")
else:
    print("please enter float values between 0.0 to 1.0)")
        

