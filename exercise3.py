a = [1,1,2,3,5,8,13,21,34,55,89]
s = input("Give me a number: ")
b = []
for x in a:
    if x < int(s):
        b.append(x)
print(b)
