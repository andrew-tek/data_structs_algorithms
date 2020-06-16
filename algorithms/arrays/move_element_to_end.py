# You're given an array of integers and an integer. Write a function that moves all instances of the integer in the array
# to the end of the array and returns the array 
#
# The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order 
# of the other integers.
#
# Sample Input
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# to_move = 2
#
# Sample Output
# [1, 3, 4, 2, 2, 2, 2] the number 1, 3, and 4 could be ordered differently 

def move_element_to_end(array, to_move):
    end_of_array = len(array) - 1
    index = 0

    while index < end_of_array:
        while index < end_of_array and array[end_of_array] == to_move:
            end_of_array -= 1
        if array[index] == to_move:
            array[index], array[end_of_array] = array[end_of_array], array[index]
        index += 1
    return array
