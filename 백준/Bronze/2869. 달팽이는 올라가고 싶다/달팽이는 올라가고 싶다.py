# 달팽이는 올라가고 싶다

import sys

input = sys.stdin.readline().split()
a = int(input[0])
b = int(input[1])
v = int(input[2])
d = 0

# 달팽이가 마지막 날에 미끄러지는 것은 상관없으니 v-b만 오르면 됨
if (v - b) % (a - b) == 0:
    print((v - b) // (a - b))
else:
    print((v - b) // (a - b) + 1)

# 시간 초과 =====================

# while v > 0:
#     d += 1
#     v -= a
#     if v <= 0:
#         print(d)
#         break
#     v += b