# 색종이 
import sys
n = int(sys.stdin.readline())
input = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = []
blue = []

def check(x, y, n):
    color = input[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            ## 만약에 색이 하나라도 첫번째 것과 다를 경우
            if color != input[i][j]:
                ## 종이를 4분할
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2)
                check(x+n//2, y+n//2, n//2)
                ## 🚨 이전에 실행 중인 'check()' 함수를 즉시 종료하고 이전 호출자에게 제어를 반환해야 함
                ## 그래야 새로운 'check()' 함수 호출이 가능
                return  
    ## 만약 색이 다 같을 경우
    if color == 0:
        white.append(n**2)
    else:
        blue.append(n**2)

check(0, 0, n)
print(len(white))
print(len(blue))