# Write a function that takes in a n x m 2-dimensional array (that can be square shaped when n == m)
# and returns a one dimensional array with all elements in spiral order. 
#
# Spiral order starts top left corner, goes to right and proceeds in a sprial pattern until all elements have been visited
#
# Input
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7
#
# Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def spiral_traverse(array):
    x_min, y_min = 0, 0
    y_max = len(array[0]) - 1
    x_max = len(array) - 1
    solution = []

    while x_min <= x_max and y_min <= y_max: 
        for i in range(y_min, y_max + 1):
            solution.append(array[x_min][i])
        for i in range(x_min + 1, x_max + 1):
            solution.append(array[i][y_max])
        for i in reversed(range(y_min, y_max)):
            if x_min == x_max: 
                break
            solution.append(array[x_max][i])
        for i in reversed(range(x_min + 1, x_max)):
            if y_min == y_max:
                break 
            solution.append(array[i][y_min])
        x_min += 1
        y_min += 1
        y_max -= 1
        x_max -= 1
    return solution
