'''Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original array
except the one at i.
For ex,if our input was [1,2,3,4,5],expected o/p would be[120, 60, 40, 30, 24].
If our input was [3,2,1], the expected output would be [2,3,6]
Follow-up: what if you can't use division? O(n)'''

import numpy as np
from timeit import default_timer as timer

def prodArray(numberList):
    start = timer()
    temp=list(numberList)
    temp1,temp2=1,1
    for i in range(len(numberList)):
        temp1=np.prod(temp[i+1:])
        if(i>0):
            temp2=np.prod(temp[0:i])
        numberList[i]=temp1*temp2
    return("Product list: ",numberList," Time taken :", timer()-start)
print(prodArray([1,2,3,4,5]))
        
