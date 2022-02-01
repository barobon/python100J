import sys
num = int(input())

points = []
for _ in range(num):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x,y])

points.sort()

for i in range(num):
    x, y = points[i]
    print(x, y)