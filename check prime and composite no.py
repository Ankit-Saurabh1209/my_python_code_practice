num = int(input("Enter any Number : "))
count = 0
for a in range(2, num):
    if num % a == 0:
        count += 1
if count >= 1:
    print(num, "is Composite Number")
else:
    print(num, "is Prime Number")
    