# 신입사원 - 그리디
import sys
T = int(sys.stdin.readline()) # 테스트 케이스의 개수

for _ in range(T):
    N = int(sys.stdin.readline()) # 지원자의 숫자
    ap = []
    now = float("inf")
    count = 0
    for _ in range(N):
        ap.append(list(map(int, sys.stdin.readline().split())))
    ## 서류심사 성적을 기준으로 정렬
    ## 다음 지원자는 항상 전 지원자보다는 서류심사 성적이 낮음
    ## 그래서 면접 심사는 높아야 함
    ap.sort()
    for i in ap:
        ## 면접 심사 점수가 전 지원자보다 높은지
        if now > i[1]:
            now = i[1]
            count += 1
    print(count)