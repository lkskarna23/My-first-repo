# Minutes to Hours: Prompt for an integer representing munutes and  output .how many hours and remaing minutes that equals (using // and %)
min= int(input())
hour=min//60
rmin=min%60

print(f"{hour}hr {rmin}minute")


