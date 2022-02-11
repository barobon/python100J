from collections import deque

que = deque(list(range(3)))

while que:
    print(que.pop())