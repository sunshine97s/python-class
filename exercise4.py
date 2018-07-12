number_str = input("Please input a number: ")
number =int(number_str)
x = range(2,number-1)
divisor = []
divisor.append(1)
for element in x:
    if number % element == 0:
        divisor.append(element)
divisor.append(number)
print(divisor)
