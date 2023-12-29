function solution(n) {
    let answer = '';
    const one = "수"
    const two = "수박"
    for (let i = 0; i < Math.floor(n/2); i++){
        answer += two
    }
    if (n % 2 != 0){
        answer += one
    }
    return answer;
}