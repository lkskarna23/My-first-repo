#29. **Max of Three Function:** Write a function `max_of_three(a, b, c)` that returns the largest value using nested `if` statements (no built-in `max()`).
def maxi(a,b,c):
    if a!=b and a!=c and b!=c:
        if(a>b>c):
            print(a,"a is larger")
        elif b>c>a:
            print(b,"b is larger")
        elif c>a>b:
            print(c,"c is larger")

    elif a==b and b>c and a>c:
        print(a,"",b,"Both a and b are larger")
    elif a==c and a>b and c>b:
        print(a,"",c,"Both a and c are larger")
    elif b==c and b>a and c>a:
        print(b,"",c,"Both b and c are larger")
    else:
        print(a,b,c,"ALL ARE EQUAL")

maxi(int(input("a : ")),int(input("b : ")),int(input("c : ")))
