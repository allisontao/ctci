# There are three types of edits that can be performed on strings: insert a character, remove a character,
# or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

s1 = "pal"
s2 = "pale"


def check_replace(first, second):
    found_diff = False
    for i in range(len(first)):
        if first[i] != second[i]:
            if found_diff:
                return False
            found_diff = True
    return True


def check_insert(first, second):
    index1 = 0
    index2 = 0
    while index1 < len(first) and index2 < len(second):
        if first[index1] != second[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def one_away(s1, s2):
    if len(s1) == len(s2):
        return check_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return check_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return check_insert(s2, s1)
    return False


print(one_away(s1, s2))
