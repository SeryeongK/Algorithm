function solution(a, b, n) {
    var answer = 0;
    while(n >= a){
        empty = Math.floor(n / a)
        answer += empty * b
        n += (empty * b)
        n -= (empty * a)
    }
    return answer;
}