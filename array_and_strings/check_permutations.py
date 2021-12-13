# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

p1 = 'ate'
p2 = 'tea'

# sort
def check_permutations(p1, p2):
    x = sorted(p1)
    y = sorted(p2)
    if x == y:
        return True
    return False

# compare number of letters (maps)
def check_permutations2(p1, p2):
    a = {}
    b = {}
    for letter in p1:
        if letter in a:
            a[letter] += 1
        else:
            a[letter] = 1
    for letter in p2:
        if letter in b:
            b[letter] += 1
        else:
            b[letter] = 1
    if a == b:
        return True
    return False

print(check_permutations(p1, p2))
print(check_permutations2(p1, p2))