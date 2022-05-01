from collections import deque

que = deque(list(range(3)))

while que:
    print(que.pop())

nums = list(range(4))
print(nums)

while nums:
    print(nums.pop())