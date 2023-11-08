function solution(s) {
    var answer = '';
    let half = Math.floor(s.length / 2)
    if (s.length % 2 === 0){
        answer = s.slice(half-1, half+1)
    } else {
        answer = s[half]
    }
    return answer;
}