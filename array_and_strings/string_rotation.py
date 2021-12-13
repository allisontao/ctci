# String Rotation:Assumeyou have a method isSubstring which checks if one word is a substring of another. Given two
# strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring (e.g.,
# "waterbottle" is a rotation of"erbottlewat").

def is_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
    return False
