#length=len(word)
#print("the input = " + word)
#print("the output of length number = " + word[length::-1])
#print("the output of reversed word is " +  word[::-1])
word = input("Please input a word: ")
a = word[::-1]
print(a)
if a == word:
        print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")








