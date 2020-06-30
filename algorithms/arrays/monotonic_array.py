# Write a function that takes in an array of integers and returns a boolean representing
# whether the array is monotonic.
#
# An array is sait to be monotonic if its elements, from left to right, are entirely non=increasing or 
# entirely non-decreasing.
#
# Sample Input:
# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
#
# Sample Output:
# True

def is_monotonic(array):
    if len(array) == 1:
        return True
    increasing = is_increasing(array)
    if increasing:
        prev = array[0]
        index = 1
        while index < len(array):
            if prev <= array[index]:
                prev = array[index]
                index += 1
            else:
                return False
        return True
    elif increasing == False:
        prev = array[0]
        index = 1
        while index < len(array):
            if prev >= array[index]:
                prev = array[index]
                index += 1
            else:
                return False
        return True
    else:
        return True

def is_increasing(array):
    index = 1
    prev = array[0]
    while index < len(array):
        if prev < array[index]:
            return True
        elif prev > array[index]:
            return False 
        elif prev == array[index]:
            index += 1

if __name__ == '__main__':
    array = [-1, -5, -10, -1100, -1100, -1101, 1102, -9001]
    print(is_increasing(array))