import sys

def lowerBS(target, lst):
    start = 0
    end = len(lst) - 1
    while(start<end):
        mid = (start + end)//2
        if(lst[mid]>=target):
            end = mid
        else:
            first = mid + 1
    return mid

def upperBS(target, lst):
    start = 0
    end = len(lst) - 1
    while(start<end):
        mid = (start + end)//2
        if(lst[mid]>target):
            end = mid 
        else:
            first = mid + 1
    return mid


N = int(input())
listN = list(map(int, sys.readline().split()))
listN.sort()    #이진탐색할 리스트이므로 정렬

M = int(input())
listM = list(map(int, sys.readline().split()))
lenM = len(listM)

for i in range(M):
    lower = lowerBS(listM[i], listM)
    upper = upperBS(listM[i], listM)