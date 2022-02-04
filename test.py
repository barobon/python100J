import sys
tmp = []
while True:
    people = list(map(str, sys.stdin.readline().split()))
    people[0] = int(people[0])
    tmp.append(people)
    print(tmp)
