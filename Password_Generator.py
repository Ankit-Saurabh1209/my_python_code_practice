import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number =  "1234567890"
symbol = "!@#$%678()?/*"

use_for = lower_case + upper_case + number + symbol

len_of_pass = 10

password = "".join(random.sample(use_for, len_of_pass))
print(password)