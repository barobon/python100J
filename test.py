from collections import deque

que = deque([[0, 1]])

while que:
    p = []
    p = que.pop()
    print(p)
    num = p[0] + 1
    print(num)


print('end')