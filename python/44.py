#44.**The Chapter 5 Classic (Exercise 1):** Repeatedly read numbers until the user enters `"done"`. Once `"done"` is entered, print `total`, `count`, and `average`. If
#the user enters anything other than a number or `"done"`, detect the mistake with `try/except`, print `"Invalid input"`, and skip to the next number.



count=0
total=0
avg=0
while True:
    num=input("enter value : ")
    if num=="done":
        print(count,"count : ")
        print(total,"total : ")
        print(avg,"avg : ")
    
        break
    try:
        num=int(num)
        count=count+1
        total=total+num
        avg=total/count
       
    

        
        
      
    except:
        print("invalid value")
