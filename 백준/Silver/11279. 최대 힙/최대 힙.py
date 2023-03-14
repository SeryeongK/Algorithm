# 최대 힙 - 힙
import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
	input = int(sys.stdin.readline())
	## 배열에 값이 있고 x가 0일 때
	if heap and input == 0:
		## 🚨 heap에서 음수로 빼오기(원상복귀)
		print(-heapq.heappop(heap))
	## x가 자연수일 때
	elif input != 0:
		## 🚨 heap에 음수로 추가(우선 순위가 반대로)
		heapq.heappush(heap, -input)
	## 배열에 값이 없고 x가 0일 때
	else:
		print(0)