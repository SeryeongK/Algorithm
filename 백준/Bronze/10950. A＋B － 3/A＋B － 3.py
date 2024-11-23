T = int(input())
input = [input() for _ in range(T)]

for i in input:
    a, b = map(int, i.split())
    print(a + b)