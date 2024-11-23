T = int(input())
input = [input() for _ in range(T)]

for i in input:
    num, word = i.split()
    words = list(word)
    result = []
    for letter in words:
        result.append(letter * int(num))
    print(''.join(result))