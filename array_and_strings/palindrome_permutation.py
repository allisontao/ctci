s1 = "tact coa"


def palindrome_permutation(s):
    s = s.replace(" ", "")
    m = {}
    for i in range(len(s)):
        if s[i] in m:
            m[s[i]] += 1
        else:
            m[s[i]] = 1
    print(m)
    count = 0
    for value in m.values():
        if value % 2 != 0:
            count += 1

    if count > 1:
        return False

    return True


print(palindrome_permutation(s1))
