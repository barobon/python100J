import sys      #오류나면 사용 중인 에디터 관리자로 실행
from queue import PriorityQueue
# 노드 수, 간선의 수, 거리, 노드 번호
N, M, K, X = map(int, sys.stdin.readline().split())      

#입력값이 많을 때 input() 사용 시 시간초과가 발생할 수 있음
worldMap = [[] for _ in range(N+1)]   #이중리스트로 그래프 생성
for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    worldMap[node1].append((node2, 1))  #가중치 1


distance = [int(1e9)] * (N+1)       #시작점과 각 도시들의 거리 비용 리스트를 아주 큰 수로 초기화

def dijkstra(start):
    distance[start] = 0
    pq = PriorityQueue(maxsize= M)
    pq.put((0, start))

    while not pq.empty():
        dis, current =  pq.get()    #시작점에서 현재 위치까지 오는데 필요한 비용. 현재 위치
        if(distance[current] < dis):    #기존의 최소비용(시작점에서 직통으로 다른 도시까지 갈 때 필요한 비용)이 다른 도시를 거치고 간 거리보다 짧으면 반복문 앞으로 돌아감.
             continue
        
        for city in worldMap[current]:
            cost = dis + city[1]    #현재 위치까지 필요한 비용 + 다음 도시까지의 비용
            if(cost < distance[city[0]]):
                distance[city[0]] = cost    #최소비용 갱신
                pq.put((cost, city[0]))   #시작점 - 인접 도시까지의 비용, 인접 도시 push

dijkstra(X)
answer = []

for i in range(N+1):
    if(distance[i] == K):
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)