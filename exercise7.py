a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = []
for element in a:
    if element % 2 == 0:
        b.append(element)
print(b)


c = [somenumber for somenumber in a if somenumber % 2 == 0]
print(c)