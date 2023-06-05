def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i, citation in enumerate(citations):
        if citation <= i:
            break
        answer += 1
    return answer
