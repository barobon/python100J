import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    que = deque([[x,y]])
    field[x][y]=0
    while que:
        point = []
        point = que.pop()
        for i in range(4):
            q = point[0] + dx[i]
            w = point[1] + dy[i]
            if 0 <= q < M and 0 <= w < N and field[q][w] == 1:
                field[q][w] = 0
                que.append([q, w])

T = int(input())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * N for _ in range(M)]
    count = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y]=1
    
    for i in range(M):
        for j in range(N):
            if(field[i][j]==1):
                bfs(i,j)
                count += 1
    print(count)





