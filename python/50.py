#50. **Total & Grade Summary:** Write a program that takes student test scores one by one until `"done"` is typed. Calculate the average score, then pass that average
# into your `computegrade()` function from Exercise 27 to print the final class letter grade. Protect against invalid score inputs with `try/except`.

count=0
total=0
avg=0

while True:
    cmd=input("enter grade :  ")
    if cmd=="done":
        if grade<0.9:
            print("grade : A")
        elif grade<0.8:
            print("grade : B")
        elif grade<0.7:
            print("grade : C")
        elif grade>0.6:
            print("grade : D")
        print("avg is : ",avg)
        break
    try:
        grade=float(cmd)
        count=count+1
        total=total+grade
        avg=total/count

    except:
         print("unable to conver value")

                    
                    
