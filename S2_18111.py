import sys
N, M, B = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minTime = int(1e11)
maxHeight = -1

for h in range(0, 257):
    tmpTime = 0
    stackNum =0
    delNum =0
    for i in range(N):
        for j in range(M):
            if(h - ground[i][j] >= 0):
                stackNum += h - ground[i][j]
            else:
                delNum += ground[i][j] - h

    if(B<stackNum-delNum):
        continue
    tmpTime = stackNum + delNum * 2
    if(tmpTime <= minTime):
        minTime = tmpTime
        maxHeight = h
print(minTime, maxHeight)