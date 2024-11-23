T = int(input())
input = [input() for _ in range(T)]

for result in input:
    result = list(result)
    score = 0
    continuedScore = 0
    for i in result:
        if i == 'O':
            continuedScore += 1
            score += continuedScore
        else:
            continuedScore = 0
    print(score)