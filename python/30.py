#30. **Even Checker Function:** Write a function `is_even(n)` that returns `True` if `n` is even and `False` otherwise.

def is_even(num):
    if num%2==0:
        return True
    else:
        return False

print(is_even(int(input("Enter Number To Check Whether it id odd or even : "))))
    
