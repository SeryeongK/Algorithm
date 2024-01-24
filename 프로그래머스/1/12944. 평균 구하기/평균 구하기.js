function solution(arr) {
    let answer = 0;
    for (a of arr){
        answer += a
    }
    return answer / arr.length;
}