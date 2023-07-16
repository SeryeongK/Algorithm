import sys
N, M = map(int, sys.stdin.readline().split())

package = []
string = []

# 패키지와 낱개 따로 넣기
for _ in range(M):
    p, s = map(int, sys.stdin.readline().split())
    package.append(p)
    string.append(s)

package.sort()
string.sort()
answer = 0

if N >= 6:
    p = N // 6
    s = N % 6

    answer = min((p+1) * package[0], p *
                 package[0] + s * string[0], N * string[0])
else:
    answer = min(package[0], string[0]*N)

print(answer)
