#48. **Odd Number Collector:** Loop through numbers from 1 to 50. Use `continue` to skip all even numbers, and print only the odd numbers.


odd=[]
for i in range(51):
    if i%2==0:
        continue
    else:
        odd.append(i)
        print(i,end=",")

        
