# 열 개씩 끊어 출력하기
import sys

input = sys.stdin.readline()

for i in range(0, len(input), 10):
    print(input[i:i+10])