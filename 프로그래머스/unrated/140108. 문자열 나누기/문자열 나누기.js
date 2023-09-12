function solution(s) {
    let same = 0
    let dif = 0
    let stack = []
    let answer = 0
    for (word of s){
        if (stack[0] == word || stack.length == 0){ // x와 같은 글자일 경우
            stack.push(word)
            same ++
        } else { // x와 다른 글자일 경우
            stack.push(word)
            dif ++
        }
        // x와 x가 아닌 다른 글자들이 나온 횟수가 같을 때
        if (same == dif){
            answer ++
            while(stack.length > 0){
                stack.pop()
            }
        }
    }
    // 두 횟수가 다른 상태에서 읽을 글자가 없을 경우
    if (stack.length > 0){
        answer ++
    }
    return answer;
}