# Given an array of integers, return the indices of the two numbers whose sum is equal to a given target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example: Given nums = [2, 7, 11, 15], target = 9
# The output should be [0, 1]. 
# Because nums[0] + nums[1] = 2 + 7 = 9.

def two_number_sum(array, targetSum):
    array.sort()
    currentStart = 0
    currentEnd = len(array) - 1
    while currentStart != currentEnd:
        currentSum = array[currentStart] + array[currentEnd]
        if currentSum == targetSum:
            return [array[currentStart], array[currentEnd]]
        elif currentSum < targetSum:
            currentStart = currentStart + 1
        elif currentSum > targetSum:
            currentEnd = currentEnd - 1
    return []
    
