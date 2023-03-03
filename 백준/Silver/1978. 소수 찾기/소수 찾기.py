# 소수 찾기
import sys

n = int(sys.stdin.readline())
line = sys.stdin.readline().split()

count = 0

for i in range(n):
    # 🚨 변수 초기화 위치 조심하기
    e = 0
    if int(line[i]) != 1:
        for j in range(2, int(line[i])):
            if int(line[i]) % j == 0:
                e += 1
        if e == 0:
            count += 1
                
print(count)