# 아침 산책 - DFS
"""
실외를 한 덩어리라고 치고 실외를 기준으로 한 실내의 순열 개수를 구하는 것
"""

import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline()) ## 정점의 수
data = sys.stdin.readline() ## 실내인지 실외인지
roads = [[] for _ in range(N+1)] ## 간선의 수
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    roads[a].append(b)
    roads[b].append(a)

def DFS(start):
    # print(start)
    visited[start] = 1
    temp = 0 # 지역변수로 바꿔주기
    for i in roads[start]:
        # print(i)
        ## 실외이면
        if int(data[i-1]) == 0:
            if not visited[i]:
                visited[i] = 1
                temp += DFS(i)
        ## 🚨 실내이면(방문 확인할 필요도 없음!!!)
        else:
            temp += 1
    # print("indoor: ", temp)
    return temp

visited = [0] * (N+1)
indoor = 0
total = 0
for i in range(1, N+1):
    ## 방문 안 했고 실외이면
    if (visited[i] == 0) and (int(data[i-1]) == 0):
        # print(f'start {i}')
        indoor = DFS(i)
        total += indoor*(indoor-1)

ii = 0
## 실내-실내
for i in range(1, N+1):
    for j in roads[i]:
        if int(data[i-1]) == 1 and int(data[j-1]) == 1:
            ii += 1

# print("indoor:", indoor, "i:", ii)
print(total + ii)