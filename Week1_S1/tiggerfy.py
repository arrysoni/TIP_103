"""
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.


word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
Example Output:

"r"
"eplan"
"chor"

"""

"""
Understand:
    Input: String
    Output: String with substrings removed
	
If we encounter:
1. g-> check if next char is g, remove gg
2. e-> check if next char is r, remove er

Edge:
1. Empty string-> return empty string itself
2. ttiiggggerer -> ""

Plan:

Pointer based-mechanism
Create a new string where we store the rest of the string
"""
# Case insensitsive, removes substrings "t" "i" "gg" "er"


def tiggerfy(word):
    word = word.lower()
    left = 0
    new_str = ""

    while left < len(word):
        if word[left] == 't' or word[left] == 'i':
            left += 1
        elif word[left] == 'g' and left + 1 < len(word) and word[left + 1] == 'g':
            left += 2
        elif word[left] == 'e' and left + 1 < len(word) and word[left + 1] == 'r':
            left += 2
        else:
            new_str += word[left]
            left += 1

    return new_str

word1 = "Trigger"
print(tiggerfy(word1))

word2 = "eggplant"
print(tiggerfy(word2))

word3 = "Choir"
print(tiggerfy(word3))
