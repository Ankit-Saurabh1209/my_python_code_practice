def is_leap(Year):
    leap = False
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = False
    else:
        leap = False

    return leap


year = int(input())

print(is_leap(year))
