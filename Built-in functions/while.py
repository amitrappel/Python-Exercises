__author__ = 'Amit Rappel'

# Find how to change money into smaller money

values = [100, 50, 10, 5, 1, 0.5, 0.1, 0.05, 0.01]
amount = 197.47

change = {}
for value in values:
    change[value] = 0
    while amount >= value:
         change[value] += 1
         amount -= value

print change