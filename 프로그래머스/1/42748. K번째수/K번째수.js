function solution(array, commands) {
    let answer = [];
    for (c of commands){
        const i = c[0]
        const j = c[1]
        const k = c[2] - 1
        answer.push(array.slice(i-1, j).sort((a, b) => a - b)[k])
    }
    return answer;
}