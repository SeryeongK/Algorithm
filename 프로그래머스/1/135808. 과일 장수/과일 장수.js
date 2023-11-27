function solution(k, m, score) {
    let answer = 0;
    score = score.sort((a, b) => b - a)
    const scoreLen = score.length
    score = score.slice(0, scoreLen - (scoreLen % m))
    for (let i = 0; i < Math.floor(scoreLen / m); i++){
        const temp = score[i*m+m-1]
        answer += temp * m
    }
    return answer;
}