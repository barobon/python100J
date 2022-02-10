import sys

def dfs(node, depth, count):
    visited[node] = 1
    print(visited)
    depth += 1
    for i in range(N):
        if visited[i] == 0 and graph[node][i] == 'Y':
            count += 1
            if depth < 2:
                count = dfs(i, depth, count)
    return count

N = int(input())
graph = []
friend = [0]*N
for _ in range(N):
    #rstrip로 줄바꿈 삭제
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    depth = 0
    count = 0
    visited = [0]*N
    count = dfs(i, depth, count)
    print(count)
    friend[i] = count

print(friend)
