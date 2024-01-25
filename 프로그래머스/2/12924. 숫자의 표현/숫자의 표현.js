function solution(n) {
    let answer = 1;
    let start = 1
    let end = 1
    let sum = 1
    while (start < n && end < n){
        if (sum === n){
            answer += 1
            sum -= start
            start += 1
        } else if (sum < n){
            end += 1
            sum += end
        } else {
            sum -= start
            start += 1
        }
    }
    return answer;
}