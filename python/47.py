#47. **Password Gatekeeper:** Write a `while True` loop that repeatedly asks for a password. If the input matches `"python123"`, print `"Access Granted"` and `break`.
# If they fail 3 times, terminate with `"Locked out"`.


count=0

while True:
    password=input("enter password  : ")
    count=count+1
    if password=="karna":
        print("Access Granted")
        break
    if count==3:
        print("locked out")
        quit()
