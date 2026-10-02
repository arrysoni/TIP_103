"""
As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the right range of buyers. A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.


Example Output:
5
Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

2
0

Understand:
1. We are returning the "length" NOT THE SUBSTRING: keep a counter (max)
2. 2 pointer : (may or may not be sliding window)

# max - min = 1 
# track max and min 

Plan:

- build a map (dictionary) that has the number has the key, and its number of appeareances as the value 
{1:1}
{2:3}
{3:2}
{5:1}
{7:1}

-max_len: __ 
-temp:___

-- temp: 3
-- temp: 3+2. = 5

- loop through the keys of the map, 
- for each key 
- increment temp by the value of the key itself
- consider the key to be the min, increment temp by the value of (key + 1) --> also assuming that key + 1 exists 
- update max 
-return max 



Br

[]

[1,3,2,2,5,2,3,7]. count = 1 + 1 + 1 + 1

l = 0
r = 1
temp = [] / temp += 1 (if abs(right - left) == 1): right += 1

while r < len(lst):

 if (abs(lst[r] - lst[l])) <= 1):
 count += 1

 else:
 l += 1

 r += 1




Implement:
"""



def find_balanced_subsequence(art_pieces):

    # Create a hash map where key: values = art_peice_price: # of times it appears

    dict_arts = {}
    max_len = 0
    temp = 0


    for art in art_pieces:
        dict_arts[art] = dict_arts.get(art, 0) + 1

    if (len(dict_arts) <= 1):
        return max_len

    for k in dict_arts:
        temp += dict_arts[k]
        if (k+1) in dict_arts: 
            temp += dict_arts[k+1]
        if temp > max_len:
            max_len = temp
        temp = 0

    return max_len

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))
