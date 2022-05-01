T = int(input())

for _ in range(6):
    PS = input()
    stack =[]

    for p in PS:
        if p == '(':
            stack.append(p)
        elif p == ')' and stack:
            stack.pop()
        elif p == ')'and not stack:
            print("NO")
            break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")


