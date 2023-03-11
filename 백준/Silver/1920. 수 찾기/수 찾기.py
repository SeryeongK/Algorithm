# # 수 찾기 (시간 초과)
# import sys

# n = int(sys.stdin.readline())
# a = sorted(list(map(int, sys.stdin.readline().split())))
# m = int(sys.stdin.readline())
# input = list(map(int, sys.stdin.readline().split()))

# for i in range(m):
#     if input[i] in a:
#         print(1)
#     else:
#         print(0)

# 수 찾기(이진 탐색)
import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))

# 재귀함수
def binary_search(array, target, start, end):
		if start > end:
			return None
		mid = (start + end) // 2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			return binary_search(array, target, start, mid - 1)
		else:
			return binary_search(array, target, mid + 1, end)

for i in range(m):
	result = binary_search(a, input[i], 0, n - 1)
	if result == None:
		print(0)
	else:
		print(1)