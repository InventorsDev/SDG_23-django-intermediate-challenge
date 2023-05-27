######################################################################################
############################## Question 1: ###########################################
#### Write a function called getMaxSum that takes a list of integers as input ########
#### Return: the maximum sum of any contiguous subarray of the given array. If the
#### array is empty or contains only negative integers, the function should return 0.
######################################################################################

def getMaxSum(array):
    if not array or max(array) < 0:
        return 0

    max_sum = array[0]
    current_sum = array[0]

    for i in range(1, len(array)):
        if current_sum < 0:
            current_sum = array[i]
        else:
            current_sum += array[i]
            max_sum = max(max_sum, current_sum)

    return max_sum

######################################################################################
############################## Question 2: ###########################################
#### Write a function called uniqueChars that takes a string as input ################
#### Return: a new string containing only the unique characters in the input string,
#### in the order that they first appear. If the input string is empty or contains
#### only whitespaces, the function should return an empty string.
######################################################################################

def uniqueChars(string):
    unique_letters = ""
    if string.isspace() or string == "":
        return ""
    else:
        for letter in string:
            if letter not in unique_letters:
                unique_letters += letter
    return unique_letters
a = uniqueChars(" \t ")
print(a)