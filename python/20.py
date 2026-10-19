#20. **Triangle Validator:** Prompt for three side lengths; check if they can form a valid triangle ($a + b > c$, $a + c > b$, $b + c > a$).
a=int(input("enter len for a "))
b=int(input("enter len for b "))
c=int(input("enter len for c "))

if (a+b)>c and (a+c)>b and (b+c)>a:
    print("they can for triangle")

else:
    print('they cannot form triangle')
    
