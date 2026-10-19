#38. **List Counter:** Given a list `[9, 41, 12, 3, 74, 15]`, write a `for` loop that counts the total number of items without using `len()`.
length=0
a=[9,41,12,3,74,15]
for i in a:
    print(i)
    length=length+1
print("total numbers in the list ",length)
