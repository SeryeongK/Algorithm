import sys
input = sys.stdin.readline

N,K = map(int,(input().split()))
X = sorted([int(input().rstrip()) for _ in range(N)])

l, r = min(X), max(X)+K

def calc(lst, m):
    t = 0
    for num in lst:
        if num >= m:
            break
        t += m-num
    return t

while l <= r:
    m = (l+r)//2
    if calc(X,m) <= K:
        res = m
        l = m+1
        
    else:
        r = m-1

print(res)