# 이분 그래프 - DFS
## 이분 그래프란 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프

## 블로그 코드 참고(https://wooono.tistory.com/635)

import sys
sys.setrecursionlimit(10**6)

def DFS(start):
    global result
    for i in ls[start]:
        ## 이웃 노드에 색칠되어있지 않다면
        if visited[i] == -1:
            ## 기준 노드와 다른 색으로 색칠하기
            if visited[start] == 1:
                visited[i] = 2
            if visited[start] == 2:
                visited[i] = 1
            DFS(i)
        # 이웃 노드에 색칠이 되어 있다면
        else:
            if visited[start] == visited[i]:
                result = False
                return 

K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    input = []
    for _ in range(E):
        input.append(list(map(int, sys.stdin.readline().split())))
    ## 인접 리스트 만들기
    ls = [[] for _ in range(V+1)]
    for i in input:
        a, b = i
        ls[a].append(b)
        ls[b].append(a)
    ## DFS
    result = True
    visited = [-1] * (V+1)
    
    for i in range(1, V+1):
        if visited[i] == -1:
            visited[i] = 1
            DFS(i)
            ## 🚨 종료 조건 설정하기
            if result == False:
                break
    
    if result == True:
        print("YES")
    else:
        print("NO")