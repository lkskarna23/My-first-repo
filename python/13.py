#13. **Overtime Pay:** Compute gross pay where any hours worked above 40 are paid at 1.5 times the hourly rate.

d_hour=40 #defaul work hour

rate=10 #default rate per hour

d_rate=d_hour*rate #rate for 40 hours


w_hours=int(input())#worked hour

e_w_hours=w_hours-d_hour #extra hour calculation

e_rate=e_w_hours*rate*1.5

total_rate=e_rate+d_rate

print("total rate based of working hours : ",total_rate)



