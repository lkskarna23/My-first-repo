#26. **Pay Function:** Write a function `computepay(hours, rate)` that returns gross pay with overtime (1.5x over 40 hours). Call it using values from user input.

def computepay(hours,hour_pay,w_hours):
    if hours>w_hours:
        print("total pay :",hours*hour_pay)
    else:
        print("total pay : ",(w_hours-hours)*(hour_pay)*(1.5)+hours*hour_pay)

computepay(int(input("basic hour: ")),int(input('hour_pay: ')),int(input("Worked hours: ")))

