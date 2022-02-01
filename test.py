from collections import deque

que = deque([[0, 1, 2], [1,2], [2, 3, 4]])

while que:
    p = []
    p = que.pop()
    print(p)

print('end')