"""
Tag: Missing Ranges
Category: arrays / intervals
Pattern: a linear scan over sorted data, checking the gap between neighbors. Each time the gap between the previous and current value is larger than 1, you record a range.

Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.

Example Usage:

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)

clues = [-1]
lower = -1
upper = -1
find_missing_clues(clues, lower, upper)
Example Output:

[[2, 2], [4, 49], [51, 74], [76, 99]]
[]

clue	prev	clue - prev	Action
0	    -1	          1	    nothing missing
1	     0	          1	    nothing missing
3	     1	          2	    add [2, 2]
50	     3		      47    add [4, 49]
75	     50		      25    add [51, 74]
100	     75	          25    add [76, 99]
"""


def find_missing_clues(clues, lower, upper):
    result = []
    prev = lower - 1                      # pretend there's a clue just before lower

    for clue in sorted(clues) + [upper + 1]:   # sentinel just past upper
        if clue - prev > 1:               # at least one number is missing between them
            result.append([prev + 1, clue - 1])
        prev = clue

    return result


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)
