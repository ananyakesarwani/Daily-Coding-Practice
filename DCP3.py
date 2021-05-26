'''Monk loves to preform different operations on arrays, and so being the
principal of Hackerearth School, he assigned a task to his new student Mishki.
Mishki will be provided with an integer array A of size N and an integer K ,
where she needs to rotate the array in the right direction by K steps and then
print the resultant array.
As she is new to the school, please help her to complete the task.'''

'''My soultion is exceeding time limit, gotta figure out better way'''
from collections import deque
T = int(input())
while(T):
    N,K=map(int, input().split())
    rotateList=list(map(int, input().split()))
    for i in range(K):
        rotateList = deque(rotateList)
        rotateList.rotate(1)
        rotateList = list(rotateList)
    for i in range(N):
        print(rotateList[i], end=" ")
    T=T-1
