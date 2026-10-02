# Counting Treasure
'''
Captain Blackbeard has a treasure map with several clues that point to different locations on an island. 
Each clue is associated with a specific location and the number of treasures buried there. 
Given a dictionary treasure_map where keys are location names and values are integers representing 
the number of treasures buried at those locations, write a function total_treasures() that returns the 
total number of treasures buried on the island.

def total_treasure(treasure_map):
    pass
Example Usage:

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 


Understand: Sum of the values of the dictionary

Plan: Use a count to keep track of the sum

Implement:
'''
"""
def total_treasures(treasure_map):
    return sum(treasure_map.values())

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 



"""


'''
Problem 2
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message 
if it contains all of the letters in the alphabet. Given a string message containing only 
lowercase English letters and whitespace, write a function can_trust_message() 
that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

def can_trust_message(message):
    pass
Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
Example Output:

True
False

U:
# approaches: Set(), hashmap, dictionary
A letter can occur more than once
P: Count the number of keys that you have/ items in the list = 26
I: Implement using set() 

'''
"""
def can_trust_message(message):
    seen = set()
    for c in message:
        if c.isalpha():
            seen.add(c)
    return len(seen) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"
message3 = "Tr   "

print(can_trust_message(message1))
print(can_trust_message(message2))
print(can_trust_message(message3))
  
"""

'''
Captain Blackbeard has an integer array chests of length n where all
the integers in chests are in the range [1, n] and each integer appears once or twice. 
Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

def find_duplicate_chests(chests):
    pass
Example Usage:


Example Output:

[2, 3]
[1]
[]
'''


def find_duplicate_chests(chests):

    dic = {}
    res = []

    for i in range(len(chests)):
        dic[chests[i]] = dic.get(chests[i], 0) + 1

    for key, value in dic.items():
        if (value == 2):
            res.append(key)

    return res


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

'''

Captain Feathersword has found another pirate's buried treasure, but they suspect 
it's booby-trapped. The treasure chest has a secret code written in pirate language, 
and Captain Feathersword believes the trap can be disarmed if the code can be balanced. 
A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, 
Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine 
if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, 
write a function can_make_balanced() that returns True if it's possible to remove one 
letter so that the frequency of all remaining letters is equal, and False otherwise.


Example Usage:


print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 
Example Output:

True
Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

False
Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2, or vice

'''


def can_make_balanced(code):
    dic = {}
    sec_freq = {}

    # Frequencies of the letters
    for i in range(len(code)):
        dic[code[i]] = dic.get(code[i], 0) + 1

    # Frequencies of frequencies
    for key in dic.values():
        sec_freq[key] = sec_freq.get(key, 0) + 1

    if len(sec_freq) == 2:
        it = iter(sec_freq.keys())
        f = next(it)
        s = next(it)

        if sec_freq[f] == 1 or sec_freq[s] == 1:
            if abs(f - s) == 1:
                return True

    return False


{1: 1, 3: 3}
code1 = "arghhh"
code2 = "hahah"
code = "aaabbbc"

print(can_make_balanced(code1))
print(can_make_balanced(code2))
print(can_make_balanced(code))


'''
Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an island. Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these two locations is exactly equal to the amount of space left on their ship.

Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, return the indices of the two locations whose gold amounts add up to the target.

Assume that each input has exactly one solution, and you may not use the same location twice. You can return the answer in any order.

def find_treasure_indices(gold_amounts, target):
    pass
Example Usage:

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  
Example Output:

[0, 1]
[1, 2]
[0, 1]
'''
