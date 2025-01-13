import sys
T = int(sys.stdin.readline())


def binary_search(arr, target, start, end):
    # 탈출 조건
    if end < start:
        return None

    # 중간 지점
    mid = (end + start) // 2

    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)  # mid 기준 왼쪽 탐색
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)  # mid 기준 오른쪽 탐색
    else:
        return mid


for _ in range(T):
    N = int(sys.stdin.readline())
    first = sorted(list(map(int, sys.stdin.readline().split())))  # 수첩 1
    M = int(sys.stdin.readline())
    second = sys.stdin.readline().split()  # 수첩 2

    for num in second:
        if binary_search(first, int(num), 0, N-1) != None:
            print(1)
        else:
            print(0)