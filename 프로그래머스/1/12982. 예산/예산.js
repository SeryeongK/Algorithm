function solution(d, budget) {
    var answer = 0;
    d.sort((a, b) => {return a - b})
    for (depart of d){
        if(budget >= depart){
            budget -= depart
            answer += 1
        } else {
            break
        }
    }
    return answer;
}