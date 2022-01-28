N, L , W, H = map(int, input().split())
left, right = 0, max(L, W, H)   # min을 사용하면 오류나는데 원인을 잘 모르겠음

for _ in range(10000):
    mid = (left + right) / 2
    result = (L//mid) * (W//mid) * (H//mid)     # 개수는 무조건 정수여야 하기 때문에 // 사용

    if(result >= N):     # A 값이 작다
        left = mid
    else:   # A 값이 크다
        right = mid
  

print("%.11f" %(right))