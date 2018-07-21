number_str = input("Please input a number: ")
number =int(number_str)
x = range(2,number-1)
divisor = []
divisor.append(1)
for element in x:
    if number / element == 1 or number:
        print("Number is prime")
    else:
        print("Number is not prime")
        divisor.append(element)
divisor.append(number)
print(divisor)