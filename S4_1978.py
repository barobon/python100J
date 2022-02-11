from itertools import count
import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N):
    count = 0
    for j in range(1, nums[i]):
        if nums[i]%j == 0:
            count += 1
    if(count == 1):
        answer += 1
print(answer)
