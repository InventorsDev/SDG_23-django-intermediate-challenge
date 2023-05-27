######################################################################################
############################## Question 1: ###########################################
#### Write a function called getMaxSum that takes a list of integers as input ########
#### Return: the maximum sum of any contiguous subarray of the given array. If the
#### array is empty or contains only negative integers, the function should return 0.
######################################################################################

def getMaxSum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum





######################################################################################
############################## Question 2: ###########################################
#### Write a function called uniqueChars that takes a string as input ################
#### Return: a new string containing only the unique characters in the input string,
#### in the order that they first appear. If the input string is empty or contains
#### only whitespaces, the function should return an empty string.
######################################################################################

def uniqueChars(s):
    unique_chars = []
    for char in s:
        if char not in unique_chars and char != ' ':
            unique_chars.append(char)
    return ''.join(unique_chars)
