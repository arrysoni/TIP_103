def length_longestSubs(s):

    left = 0
    res = 0

    charSet = set()

    for right in range(len(s)):

            while (s[right] in charSet):
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            res = max(res, right - left + 1)

    return res


s1 = "abcabcbbb"
print(length_longestSubs(s1))

s2 = "pwwkew"
print(length_longestSubs(s2))

s3 = "zxyzxyz"
print(length_longestSubs(s3))

s4 = "xxx"
print(length_longestSubs(s4))