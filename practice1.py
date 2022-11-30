# if statement.
# if condition:
#   statement 1
#   statement 2
#   statement 3

number = 6
if number > 5:
    print(number * number)

# if-else statement.
#   if condition:
#       statement 1
#   else:
#       statement 2

password = input("Enter Password: ")
if password == "Ankit_12#>":
    print("Correct Password")
else:
    print("Incorrect Password")

# if-elif_else statement:
# if condition - 1:
#   statement 1
# elif condition - 2:
#   statement 2
# elif condition -3:
#   statement 3
# else:
#   statement 4

def user_check(choice):
    if choice == 1:
        print("Admin")
    elif choice == 2:
        print("Editor")
    elif choice == 3:
        print("Guest")
    else:
        print("Wrong entry")

user_check(1)
user_check(2)
user_check(3)
user_check(4)

# nested if-else statement:
# if condition_outer:
#    if condition_inner:
#       statement of inner
#    else:
#        statement of inner
# else:
#    statement of outer
num = 15
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# nested if statement
i = 13
if (i == 13):
    if (i < 15):
        print("i is smaller than 15")
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 12 and smaller than 15")

#Single Statement Suites
numbers = 56
if numbers > 0:
    print("Positive")
else:
    print("Negative")

#Similar to the if statement, while loop also consists of a single statement.

x = 1
while x <= 5:
    print(x, end=" ")
    x = x + 1

# for loop
# for element in sequence:
#   body for loop

for i in range(1, 10):
    print(i)

# while loop
# while condition:
#   body of while loop

num = 10
sum = 0
i = 1

while i <= num:
    sum = sum + 1
    i = i + 1
print("Sum of first 10 digit number is:", sum)

#break statement

for num in range(10):
    if num > 5:
        print("stop processing...")
        break
    print(num)

# continue statement
for num in range(3, 10):
    if num == 5:
        continue
    else:
        print(num)

# pass statement:

months =  ['Jan', 'Feb', 'March', 'April']
for mon in months:
    pass
print(months)
