function solution(n) {
    var answer = [];
    let arr = String(n).split('')
    for (a of arr){
        answer.push(Number(a))
    }
    return answer.reverse();
}