# Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array)
# whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number
# from the first array in the first position. 
#
# You can assume that there will only be one pair of numbers with the smallest difference. 
#
# Sample Input 
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
#
# Sample Output
# [28, 26]

def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()

    index_one, index_two = 0, 0
    min_value = 10000000000
    while index_one < len(array_one) and index_two < len(array_two):
        possible_min_value = abs(array_one[index_one] - array_two[index_two])
        if possible_min_value < min_value:
            min_value = possible_min_value
            solution = [array_one[index_one], array_two[index_two]]
        if array_one[index_one] > array_two[index_two]:
            index_two += 1
        else:
            index_one += 1
    return solution