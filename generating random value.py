import random

for i in range(3):
    print(random.randint(10, 20))

print(random.randint(10, 5))


members = ['Ankit', 'Annwesha', 'Surabhi']
leader = random.choice(members)
print(leader)