#35. **Multiplication Table:** Prompt for a number and print its multiplication table from 1 to 10 using a `for` loop.

n=int(input("enter number to get its multiplication table : "))
for i in range(1,11):
    print(i,"*",n,"=",n*i)
