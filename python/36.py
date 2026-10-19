#36. **Sum of N Numbers:** Prompt for a positive integer $n$ and compute the sum of all numbers from 1 to $n$ using a loop.
add=0
for i in range(int(input("enter the range "))):
    add=add+1
    add=i+add
               
print(add)

    
