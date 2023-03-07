# 그대로 출력하기 2
import sys

while True:
    try:
        # 🚨 sys.stdin.readline()는 EOF를 받을 때 빈 문자열을 리턴
        print(input())
    except EOFError:
        break