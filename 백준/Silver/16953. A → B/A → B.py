import sys

A, B = map(int, sys.stdin.readline().split())

cnt = 1
while B != A:
    if B % 2 == 0:
        B = B // 2
    elif B % 10 == 1:
        B = B // 10
    else:
        cnt = -1
        break
    cnt += 1

    if B == 0:  # A를 B로 만들 수 없을 때
        cnt = -1
        break

print(cnt)
