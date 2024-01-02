function solution(k, score) {
    let answer = [];
    let honor = []
    for (s of score){
        if (honor.length < k){
            honor.push(s)
        } else {
            if (s > honor[k-1]){
                honor.pop()
                honor.push(s)
            }
        }
        honor.sort((a, b) => b - a)
        answer.push(honor[honor.length-1])
    }
    return answer;
}