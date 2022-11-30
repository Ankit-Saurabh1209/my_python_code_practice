print("Composite Number")
start = int(input("Start no.: "))
end = int(input("End no.: "))
print("Composite numbers between", start, "and", end, "are:")

for number in range(start, end + 1):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count >= 1:
        print(number)
