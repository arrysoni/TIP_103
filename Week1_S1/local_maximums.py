"""
Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Example Usage:

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
local_maximums(grid)

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
local_maximums(grid)
Example Output:

[[9, 9], [8, 6]]
[[2, 2, 2], [2, 2, 2], [2, 2, 2]]

"""

def local_maximums(grid):
    n = len(grid)
    result = []

    for i in range(n - 2):
        row = []
        for j in range(n - 2):
            biggest = grid[i][j]          # start with the top-left cell of the 3x3 box

            for r in range(i, i + 3):     # go through the 3 rows of the box
                for c in range(j, j + 3): # go through the 3 columns of the box
                    if grid[r][c] > biggest:
                        biggest = grid[r][c]

            row.append(biggest)
        result.append(row)

    return result


grid1 = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
print(local_maximums(grid1))   # [[9, 9], [8, 6]]

grid2 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
print(local_maximums(grid2))   # [[2, 2, 2], [2, 2, 2], [2, 2, 2]]