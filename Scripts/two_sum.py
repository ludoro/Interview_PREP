"""
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.You may assume that each input would have exactly one
solution, and you may not use the same element twice.
"""
#Solution in O(n^2) trivial
#We find solution with hashtable
def two_sum(array,target):

    hashtable = {}
    index = []

    for i in range(len(array)):
        value = target - array[i]
        if value in hashtable:
            index.append([ hashtable[value], i])
        else:
            hashtable[array[i]] = i

    return index

array = [3,4,5,6]
target = 9

two_sum(array,target)
