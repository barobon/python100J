pcNum = int(input())     #컴퓨터 수
linkNum = int(input())    #연결된 쌍의 수

graph = [[0] for _ in range(pcNum+1)]   # (1, pcNum) 크기의 인접리스트 선언

for i in range(linkNum):
    x, y = map(int, input().split())    # x, y에 Pc쌍 저장
    graph[x].append(y)
    graph[y].append(x)

visited = [0 for _ in range(pcNum+1)]     # 방문 여부를 알기 위한 리스트

def dfs(node):
    visited[node] = 1   # 방문함
    for i in graph[node]:
        if(visited[i]==0):
            dfs(i)
    return

dfs(1)
visited[0] = 0
print(sum(visited)-1)   # 시작 노드 제와
pcNum = int(input())     #컴퓨터 수
linkNum = int(input())    #연결된 쌍의 수

# [0]을 pcNum+1개 만큼 생성
graph = [[0] for _ in range(pcNum+1)]   # (1, pcNum) 크기의 인접리스트 선언

for i in range(linkNum):
    x, y = map(int, input().split())    # x, y에 Pc쌍 저장
    graph[x].append(y)
    graph[y].append(x)

visited = [0 for _ in range(pcNum+1)]     # 방문 여부를 알기 위한 리스트

def dfs(node):
    visited[node] = 1   # 방문함
    for i in graph[node]:
        if(visited[i]==0):
            dfs(i)
    return True

dfs(1)
visited[0] = 0
print(sum(visited)-1)   # 시작 노드 제와
