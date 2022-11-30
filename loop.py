for x in range(3):
    for y in range(3):
        print(f'({x},{y})')

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output = output + 'x'
    print(output)


numbers = [9, 8, 7, 6, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


numbers = [9, 8, 9, 10, 7, 6, 10]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

def greet_user():
    print("Hi there!")
    print("Welcome abroad")

print("Start")
greet_user()
print("Finished")

