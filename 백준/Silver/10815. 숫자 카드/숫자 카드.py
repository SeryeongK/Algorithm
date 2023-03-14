# 숫자 카드
import sys

N = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))

output = []

def bin_search(f):
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end) //2
        if cards[mid] > f:
            end = mid - 1
        elif cards[mid] < f:
            start = mid + 1
        else:
            return True
            
for i in input:
    if bin_search(i):
        output.append(str(1))
    else:
        output.append(str(0))

print(' '.join(output))