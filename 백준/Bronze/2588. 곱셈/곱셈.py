input = [int(input()) for _ in range(2)]
a = input[0]
b = str(input[1])

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))