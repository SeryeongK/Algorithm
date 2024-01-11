function solution(n) {
    let answer = -1;
    let sqrt = Math.sqrt(n)
    for (let i=0; i <= sqrt; i++){
        if (i === sqrt){
            answer = (sqrt + 1) ** 2
        }
    }
    return answer;
}