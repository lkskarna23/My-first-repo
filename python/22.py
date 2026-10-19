#22. **Safe Integer Input:** Prompt for an integer. If the conversion fails, print `"That was not a valid number"`.




try:
    inp=int(input())
    if inp <=10:
        print(inp)
    else:
       print("that was not a valid number")
    

except:
    print("please enter number with in range of 0 to 10")
