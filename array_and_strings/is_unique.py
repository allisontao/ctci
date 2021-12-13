# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

s1 = 'hello'
s2 = 'python'
s3 = 'all'

# using a hashmap
def is_unique(string):
    m = {}
    for i in range(len(string)):
        if string[i] in m:
            return False
        m[string[i]] = 1

    return True

def is_unique2(string):
    a = sorted(string)
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    return True

print(is_unique2(s1))
print(is_unique2(s2))
print(is_unique2(s3))