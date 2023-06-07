# 히든 넘버
import sys
N = int(sys.stdin.readline())
input = list(sys.stdin.readline().strip())
alphabet = list("01231456789")
for i in range(N):
    if input[i] not in alphabet:
        input[i] = '+'

output = ''.join(input)
output = output.split('+')
answer = 0
for i in output:
    if i != '':
        answer += int(i)
print(answer)
