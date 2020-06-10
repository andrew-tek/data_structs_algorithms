#   Given two non-empty arrays of integers, write a function that determines
#   whether the second array is a subsequence of the first one.
#   A subsequence of an array is a set of numbers that aren't necessarily adjacent
#   in the array but that are in the same order as they appear in the array.

def isValidSubsequence(array, sequence):
    array_index, sequence_index = 0, 0
    while array_index < len(array) and sequence_index < len(sequence):
        if array[array_index] == sequence[sequence_index]:
            array_index += 1
            sequence_index += 1
        else:
            array_index += 1
    return sequence_index == len(sequence)