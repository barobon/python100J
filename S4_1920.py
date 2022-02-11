import sys
N= int(input())
numN = list(map(int, sys.stdin.readline().split()))
M = int(input())
numM = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if numM[i] not in numN:
        print(0)
    else:
        print(1)