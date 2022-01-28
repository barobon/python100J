#브루트 포스 알고리즘

N, M = map(int, input().split())  #직사각형의 크기 대입
rec =[]

for x in range(N):
    rec.append(input())     #rec의 각 요소에 줄바꿈 기준으로 길이 M의 리스트 추가 -> 이중리스트

# 다시 칠해야 하는 정사각형의 수를 저장하는 리스트
count = []

#체스판(8,8) 크기로 직사각형 전체 탐색
for n in range(N-7):
    for m in range(M-7):
        cntB = 0    #시작점을 B로 할지, W로 할지에 따라 결과가 달라짐
        cntW = 0
        for i in range(8):
            for j in range(8):
                if((i + j) % 2 == 0):           #체스판에서 짝수번 이동할 시 무조건 시작점과 색깔이 같다
                    if(rec[n+i][m+j] != 'B'):   #시작점을 B로 함
                        cntB += 1
                    if(rec[n+i][m+j] != 'W'):   #시작점을 W로 함
                        cntW += 1
                elif((i + j) % 2 == 1):         #체스판에서 홀수번 이동할 시 무조건 시작점과 색깔이 다르다
                    if(rec[n+i][m+j] != 'W'):   #시작점을 B로 함
                        cntB += 1
                    if(rec[n+i][m+j] != 'B'):   #시작점을 W로 함
                        cntW += 1
        count.append(cntB) 
        count.append(cntW) 

print(min(count))                       
