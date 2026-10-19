#28. **Celsius Converter Function:** Write a function `to_celsius(fahrenheit)` that takes a temperature and returns the Celsius equivalent.

def cel(fahrenheit):
    celsius=(fahrenheit-32)*(5/9)
    print(celsius)

cel(int(input("enter fahrenheit Value : ")))

