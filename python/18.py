#18. **Pass/Fail Checker:** Prompt for marks in three subjects. If all three are $\ge 40$, print `"Pass"`; if any is below 40, print `"Fail"`.

sub1=int(input("enter value for subject 1 : "))
sub2=int(input("enter value for subject 2 : "))
sub3=int(input("enter value for subhect 3 : "))

if sub1>=40 and sub2>=40 and sub3>=40:
    print("pass")
else:
    print('fail')
