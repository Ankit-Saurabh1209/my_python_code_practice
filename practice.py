a = [1, 2, 3]
b = ["one","two","three"]

for val1, val2 in zip(a, b):
    print(val1, val2)

number = 10
def func(number = 0):
    number +=90
    return number
number = 20
print(number, func(), func(10))


def cube(num):
    return num*num*num


result = cube(int(input("Cube: ")))

print(result)


print(sum(range(4, 11, 2)))


