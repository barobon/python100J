import sys

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

print(graph)