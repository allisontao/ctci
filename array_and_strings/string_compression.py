# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than
# the original string, your method should return the original string. You can assume the string has only uppercase
# and lowercase letters (a - z).

test = "aabcccccaaa"


def string_compression(s):
    s.lower()
    res = ""
    count_consecutive = 0
    for i in range(len(s)):
        count_consecutive += 1

        if i + 1 >= len(s) or s[i] != s[i+1]:
            res += s[i] + str(count_consecutive)
            count_consecutive = 0

    return res if len(res) < len(s) else s


print(string_compression(test))
