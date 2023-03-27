# 동전 0 - 그리디
import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline()))

coin = sorted(coin, reverse=True)

count = 0
for i in coin:
    if K >= i:
        count += K // i
        K = K % i
    if K == 0:
        break

print(count)