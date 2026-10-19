#49. **Running Average Monitor:** Write a loop where each valid number entered immediately displays the updated running average so far. Break on `"exit"`.


count=0
added=0

while True:
     str1=input("enter value : ")
     if str1=='exit':
         break
     try:
         num=int(str1)
         count=count+1
         added=added+num
         avg=added/count
         print("average is : ",avg)
     except:
         print("error")
    
