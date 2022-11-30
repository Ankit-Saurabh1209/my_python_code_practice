def mutate_string(string, position, character):
    lis = list(string)
    lis[position] = character
    return ''.join(lis)

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
