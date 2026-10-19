#32. **Repeat Word Function:** Write a function `repeat_lyrics(word, times)` that prints the given word that many times using a loop inside the function.

word=input("Enter words : ")
time=int(input("Enter the number to type the words : "))

for i in range(time):
    print(word)
