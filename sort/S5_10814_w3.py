import string
import sys

peopleNum = int(input())
peopleList = []

for _ in range(peopleNum):
    people = list(map(str, sys.stdin.readline().split()))
    people[0] = int(people[0])
    peopleList.append(people)

#첫번째 값을 기준으로 정렬
peopleList.sort(key=lambda x:x[0])

for i in range(peopleNum):
    print(peopleList[i][0], peopleList[i][1])