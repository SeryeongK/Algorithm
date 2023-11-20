function solution(s)
{
    let answer = -1;
    let stack = []
    for (word of s){
        if (stack.length === 0){
            stack.push(word)
        } else {
            if (stack[stack.length-1] === word){
                stack.pop()
            } else {
                stack.push(word)
            }
        }
    }
    if (stack.length > 0){
        answer = 0
    } else {
        answer = 1
    }
    return answer;
}