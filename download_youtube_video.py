#An ugly number is a positive integer whose prime factors are limited to 2, 3 and 5. Give an integer, return true if it is an ugly number.



def isUgly(n):
    if n > 0:
        factors = [2, 3, 5]
        for i in factors:
            while n % i == 0:
                n // i
        return n == 1
    else:
        return 0

n = isUgly(input("No.") )

if (n ==1):
    print("Yes")
else:
    print("No")
  

