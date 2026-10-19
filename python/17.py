#17. **Divisibility Check:** Prompt for a number and check if it is divisible by both 3 and 5.

n=int(input("enter number to check divisibility : "))

if n%3==0 and n%5==0:
    print("It is divisible by both 3 and 5")

else:
    print("It is not divisible by both 3 and 5")
