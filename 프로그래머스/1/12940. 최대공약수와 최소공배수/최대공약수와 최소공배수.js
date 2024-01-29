function solution(n, m) {
    var answer = [];
    // 최대 공약수
    for (let i = n; i > 1; i--){
        if (m % i === 0 && n % i === 0){
            answer.push(i)
            break
        }
    }
    if (answer.length === 0){
        answer.push(1)
    }
    // 최소공배수
    for (let i = n; i <= m*n; i ++){
        if (i % n === 0 && i % m === 0){
            answer.push(i)
            break
        }
    }
    return answer;
}