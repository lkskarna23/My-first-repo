#27. **Grade Function:** Write a function `computegrade(score)` that takes a float score and returns the grade string (`A`, `B`, `C`, `D`, `F`).
def grade(score):
    if score>0 and score<1:
        print("you entered the valid score")
        if score>0.9:
            pritn("grade A")
        elif score>0.8:
            print("grade B")
        elif score>0.7:
            print("grade C")
        elif score>0.6:
            print("grade D")
        else:
            print("grade F")
    else:
        print("please enter value between 0.1 to 1.0")

grade(float(input("Enter the Score : ")))     
    
