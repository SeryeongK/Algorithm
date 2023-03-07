# 음계
import sys

input = list(map(int, sys.stdin.readline().split()))

a = [1, 2, 3, 4, 5, 6, 7, 8]
d = [8, 7, 6, 5, 4, 3, 2, 1]

if input == a:
    print("ascending")
elif input == d:
    print("descending")
else:
    print("mixed")