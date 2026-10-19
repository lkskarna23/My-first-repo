#25. **Safe Temperature Converter:** Rewrite Exercise 3 to catch any non-numeric temperature values and display a helpful error message.


try:
    cel=int(input("enter celcius : "))
    faht=(cel*9/5)+32


    print(f"Fahrenheit : {faht} ")

except:
    print("please enter numeric values")
