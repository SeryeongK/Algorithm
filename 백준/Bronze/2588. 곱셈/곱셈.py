import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline()
b1 = int(b[0])
b2 = int(b[1])
b3 = int(b[2])

line1 = a * b3
line2 = a * b2
line3 = a * b1
final = a * int(b)

print(line1, line2, line3, final ,sep="\n")