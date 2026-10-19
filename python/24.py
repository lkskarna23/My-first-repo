#24. **Age Validator:** Prompt for age. Use `try/except` to convert to `int`. If valid, check if age is positive; if negative, print `"Age cannot be negative"`.
age=input()
try:
    age=int(age)
    if age>0:
        print(age)
    else:
        print("Age cannot be negative")
except:
    print("error")
