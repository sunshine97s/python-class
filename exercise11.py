def chloe(number_str):
    number = int(number_str)
    x = range(2, number)
    divisor = []
    s = ""
    divisor.append(1)
    for element in x:
        if number % element == 0:
            s = "Not the one!"
            break
        else:
            divisor.append(element)

    divisor.append(number)
    print(divisor)

    if s == "":
        return True
    else:
        return False
number_str = input("Please input a number: ")
print(chloe(number_str))

