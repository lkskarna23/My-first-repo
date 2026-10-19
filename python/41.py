#41. **Search for Item:** Given a list of numbers, use a `for` loop and a boolean flag (`found = False`) to check if the number `3` is in the list.
a=[1,2,3,4,5,6,7,8,9,10]

found=False
for i in a:
    if i==3:
        found=True
        break
if found:
    print("3 is present in the list")
else:
    print("3 is not present in the list")
   
