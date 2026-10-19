#23. **Safe Division:** Prompt for two numbers, numerator and denominator. Use `try/except` to catch `ZeroDivisionError` if the denominator is 0.

num=int(input())
den=int(input())
try:
    if den!=0:
        print(num/den)
    else:
        print("num contains zero")

except:
    print("please enter valid number")
