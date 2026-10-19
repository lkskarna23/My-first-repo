#46. **Positive-Only Sum:** Write a loop that accepts numbers continuously. If the user enters a negative number, use `continue` to ignore it. Stop when they type
#  `"stop"` and print the total of all positive numbers.

total=0
while True:
    num=input("enter value : ")
   
    if num=="stop":
        break
    try:
        num1=int(num)
       
    except:
        print("unable to convert")
    if num1<0:
        continue
    if num1>0:
        total=total+num1

print("total is : ",total)
