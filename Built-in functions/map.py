__author__ = 'Amit Rappel'


### 7 boom ###

# Option I
def boom(x):
    output = 'boom' if (x % 7 == 0 or '7' in str(x)) else x
    return output

print map(lambda x: boom, range(1, 100))

# Option II
print map(lambda x: 'boom' if (x % 7 == 0 or '7' in str(x)) else x, range(1, 100))