'''Given a list of numbers and a number k, return whether any two numbers from
the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
Do in one pass '''

''' my solution : take k and subtract each number in list from it, check if the
remainder is present in list. using set instead of list to have O(1) time
complexity while searching '''

from timeit import default_timer as timer

def sumK (numberList, k):
    numberSet = set(numberList)
    start = timer()
    for i in numberSet :
        if( k-i in numberSet):
            return("two numbers are : ", k-i, i, "Time taken : ", timer()-start)
    return("no 2 such numbers exist")
print(sumK([10, 15, 3, 7], 17))  
    

