import math
a, b, v = map(int, input().split())
# 시간 초과
# height = 0
# days = 0
# while height < v:
#     days += 1
#     height += a
#     if height >= v:
#         break
#     height -= b
print((math.ceil((v - a) / (a - b))) + 1)