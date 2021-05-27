'''Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates
and negative numbers as well.
For example, the input [3,4,-1,1] should give 2.
You can modify the input array in-place'''

'''My solution: convert into set and find the missing number by comparing with
another set of same minimum to maximum number '''

def missingValue(numList):
    numList = set(numList)
    newList = set(range(min(numList),max(numList)+1,1))
    missinList = list(newList.difference(numList))
    for i in missinList:
        if(i>0):
            return i

print(missingValue([3,4,-1,1]))
