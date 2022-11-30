def isugly(n):
    if n > 0:
        factors = [2, 3, 5]
        for i in factors:
            while n % i == 0:
                n // i
        return n == 1
    else:
        return 0

n = input("No:")

print(isugly(6))
