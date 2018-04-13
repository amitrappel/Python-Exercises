__author__ = 'Amit Rappel'

# Exercise 1:
# Concatenate the strings of a given list
my_list = ['abcde', 'fghij', 'klmn', 'opq', 'rstu', 'vwxyz']
print reduce(lambda x, y: x + y, my_list, '')

# Concatenate the numbers of a given list
my_list = [3.14, 1519]
print reduce(lambda x, y: str(x) + str(y), my_list, '')

# Get/Set a nested dictionary value
my_dict = {'k1': 'v1', 'k2': {'k21': 'v21', 'k22': 'v22', 'k23': {'k231': 'v231', 'k232': 'v232'}}}
my_key = ['k2', 'k23', 'k232']
print reduce(lambda x, y: x[y], my_key , my_dict)

# 11 divisibility
num = 109011
print reduce(lambda x, y: int(y)-int(x), str(num)[::-1]) % 11 == 0