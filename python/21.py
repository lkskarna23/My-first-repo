
#21. **Safe Pay Calculator:** Rewrite Exercise 13 so that if the user enters non-numeric input for hours or rate,
#the program prints `"Error, please enter numeric input"` and exits cleanly without crashing


try:
    d_hour=40 #defaul work hour

    rate=10 #default rate per hour

    d_rate=d_hour*rate #rate for 40 hours


    w_hours=int(input())#worked hour

    e_w_hours=w_hours-d_hour #extra hour calculation

    e_rate=e_w_hours*rate*1.5

    total_rate=e_rate+d_rate

    print("total rate based of working hours : ",total_rate)

except:
    print("please enter proper value")
