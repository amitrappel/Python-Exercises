__author__ = 'Amit Rappel'

# Find 1-9 arrangements for making Shvarim (Dudeney's "Amusements in Mathematics", problem 88

quotient = 1.0 / 3
digits = '123456789'

# Solution 1
'''
def is_permutation(num1, num2):
    return sorted(num1) == sorted(num2)

for nominator in range(5123, 9876):
    if nominator % 100 == 0: print nominator
    for denominator in range(12345, 98765):
        if is_permutation(str(nominator) + str(denominator), digits):
            if float(nominator) / denominator == quotient:
                print nominator, denominator
'''

# Solution 2
from itertools import permutations

'''
for nominator in permutations(digits, 4):
    denominator_digits = filter(lambda x: x not in nominator, digits)
    for denominator in permutations(denominator_digits):
        if float(''.join(nominator)) / float(''.join(denominator)) == quotient:
            print ''.join(nominator), ''.join(denominator)

'''
print [''.join([str(d) for d in p])+'/'+''.join([str(e) for e in q])+'='+'1/'+str(x) for p in permutations({1,2,3,4,5,6,7,8,9}, 4) for q in permutations({1,2,3,4,5,6,7,8,9}-set(p), 5) for x in range(2,3) if float(''.join([str(d) for d in p]))/int(''.join([str(e) for e in q])) == 1.0/x]
print [''.join([str(d) for d in p])+'/'+''.join([str(e) for e in q])+'='+'1/'+str(x) for p in permutations({1,2,3,4,5,6,7,8,9}, 4) for q in permutations({1,2,3,4,5,6,7,8,9}-set(p)) for x in range(2,3) if float(''.join([str(d) for d in p]))/int(''.join([str(e) for e in q])) == 1.0/x]



# more options: 1. with generator to yield denominators,
#               2. without sorted(),
#               3. find only a single solution (while)


# Verbal arithmetics (SEND + MORE = MONEY)