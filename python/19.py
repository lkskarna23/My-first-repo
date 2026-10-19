#19. **Leap Year Checker:** Prompt for a year and determine if it is a leap year (divisible by 4, not by 100 unless divisible by 400).


year=int(input("enter year : "))

if year%4==0:
    print(f"{year} is leapyear")
elif  year%400==0 and year%100!=0:
    print(f"{year}is leapyear")
else:
    print(f"{year} is not leapyear")
