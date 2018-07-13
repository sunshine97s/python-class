number = input("please input a number: ")
x = int(number)%2
if x == 0:
    print(number + " is an even number")
else:
    print(number + " is an odd number")
i = int(number)%4
if i == 0:
    print(number + " is a mutiple of 4")

#extra 2

num = input("please input a number: ")
check = input("please input another number: ")
x = int(num)
i = int(check)
if x%i == 0:
    print("answer divided evenly")
else:
    print("answer is not divided evenly")

