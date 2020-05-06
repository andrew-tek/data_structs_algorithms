# Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. If there is such a triplet present in array, then print the triplet and return true. Else return false.
# Example:

# Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
# Output: 12, 3, 9
# Explanation: There is a triplet (12, 3 and 9) present
# in the array whose sum is 24. 

# Input: array = {1, 2, 3, 4, 5}, sum = 9
# Output: 5, 3, 1
# Explanation: There is a triplet (5, 3 and 1) present 
# in the array whose sum is 9. 

def three_number_sum(array, target_sum):
    array.sort()
    solutions = []
    for i in range(len(array) - 2):
        start = i + 1
        end = len(array) - 1
        while start < end:
            current_sum = array[i] + array[start] + array[end]
            if target_sum == current_sum:
                solutions.append([array[i], array[start], array[end]])
                start += 1
                end -= 1
            elif target_sum < current_sum:
                end -= 1
            elif target_sum > current_sum:
                start += 1
    return solutions
