# 하노이의 탑
import sys

n = int(sys.stdin.readline())
k = 0

def hanoi(num, start, end, middle):
    global k
    if num == 0:
        pass
    else:
        hanoi(num-1, start, middle, end)
        print(f"{start} {end}")
        k += 1
        hanoi(num-1, middle, end, start)

## 하노이의 탑은 1개일 때 1, 2개일 때 3, 3개일 때 7 ... 계차 수열 => 2**n -1
print(2**n -1)
if n <= 20:
    hanoi(n, 1, 3, 2)