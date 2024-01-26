import random

# Even random number generator from 1-10
num_list = [2, 4, 6, 8, 10]
random_num = random.choice(num_list)

print(f"Random Even Number: {random_num}")

random_num = random_num / 2

print(f"Random Even Number Divided by 2: {random_num}")
