#37. **Factorial Calculator:** Prompt for a number $n$ and calculate its factorial ($n! = n \times (n-1) \times \dots \times 1$) using a loop

fact=1
inp=int(input())
for i in range(1,inp+1):
    fact=fact*i
print(fact)
