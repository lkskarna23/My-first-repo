#45. **Min-Max Extractor (Exercise 2):** Repeatedly read numbers until the user enters `"done"`. At the end, print both the maximum and minimum numbers entered. Handle
#bad input using `try/except`.

largest=None
smallest=None

while True:
    num=input("enter value : ")
    if num=="done":
       
        
        
        break
    try:
        num1=int(num)
    
       
        
    except:
        print("invalid input")

    if largest==None or largest<num1:
        largest=num1


    if smallest==None or smallest>num1:
        smallest=num1
print("smallest number is  ",smallest)

print("largest is numger is ",largest)
