function solution(arr, queries) {
    var answer = [];
    for (q of queries){
        let array = [...arr].slice(q[0], q[1]+1).sort((a, b) => a - b)
        let push = false
        for (a of array){
            if (q[2] < a){
                answer.push(a)
                push = true
                break
            }
        }
        if (!push){
            answer.push(-1)
        }
    }
    return answer;
}