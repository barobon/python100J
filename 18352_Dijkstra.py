import imp
import sys      #오류나면 사용 중인 에디터 관리자로 실행
import heapq
# 노드 수, 간선의 수, 거리, 노드 번호
N, M, K, X = map(int, sys.stdin.readline().split())      

#입력값이 많을 때 input() 사용 시 시간초과가 발생할 수 있음
worldMap = [[] for _ in range(N+1)]   #이중리스트로 그래프 생성
for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    worldMap[node1].append(node2, 1)  #가중치 1

distance = [int(1e9)] * (N+1)       #시작점과 각 도시들의 거리 비용 리스트를 아주 큰 수로 초기화

def dijkstra(start):
    distance[start] = 0

