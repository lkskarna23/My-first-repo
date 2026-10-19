#Gross pay calculator:prompt the user for hours worked andr rate per hour, then calculate and  print totalpay

w_hours=int(input())

rate_p_hr=int(input())

total_wages=w_hours*rate_p_hr

print(f"Worked Hours {w_hours} ")
print(f"Rate per hour{rate_p_hr}")
print(f"total pay {total_wages}")
