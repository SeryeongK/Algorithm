# 외판원 순회 - DP, DFS, 비스마스킹
# 블로그 코드 참고(https://hongcoding.tistory.com/83)
import sys

N = int(sys.stdin.readline()) # 도시의 수
graph = [] # 비용 행렬 지도
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

INF = float("inf")
# 행 번호는 도시, 열 번호는 visited    
DP = [[0 for _ in range((1 << N) - 1)] for _ in range(N)]

def DFS(start, visited):
    if visited == (1 << N) - 1: # 모든 도시를 방문했으면
        if graph[start][0]: # 마지막 경로에서 가장 끝(시작)인 0번 도시로 갈 수 있으면
            return graph[start][0]
        else:
            return INF
    
    # 이미 최소비용이 계산되어 있다면(또 할 필요 없음)
    if DP[start][visited] != 0:
        return DP[start][visited]
    
    DP[start][visited] = INF
    # 도시 가기
    for i in range(1, N): # 0번 도시는 이미 처음에 갔기 때문에
        # 갈 수 없다면
        if graph[start][i] == 0:
            continue
        # 이미 가봤다면
        if visited & (1 << i):
            continue
        DP[start][visited] = min(DP[start][visited], graph[start][i]+DFS(i, visited | (1 << i)))

    return DP[start][visited]

print(DFS(0, 1))
