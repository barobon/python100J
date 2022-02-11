import sys

def dfs(node, depth):
    depth += 1
    count = 0
    for i in range(N):
        if visited[i] == 0 and graph[node][i] == 'Y':
            count += 1
            visited[i] = 1
            if depth < 2:
                count += dfs(i, depth)
    return count

N = int(input())
graph = []
for _ in range(N):
    #rstrip로 줄바꿈 삭제
    graph.append(list(sys.stdin.readline().rstrip()))

maxF = 0

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    depth = 0
    maxF = max(maxF, dfs(i, depth))

print(maxF)
