function solution(score) {
    let answer = [];
    let sum = []
    for (s of score){
        sum.push((s[0] + s[1]) / 2)
    }
    let orderedSum = [...sum]
    orderedSum.sort((a, b) => b - a)
    
    for (s of sum){
        answer.push(orderedSum.indexOf(s)+1) 
    }
    return answer;
}