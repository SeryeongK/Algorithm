def solution(s):
    s = list(s)
    answer = []
    answer.append(s[0].upper())
    for i in range(1, len(s)):
        if s[i] == " ":
            answer.append(s[i])
        elif answer[-1] == " ":
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
    answer = "".join(answer)
    return answer