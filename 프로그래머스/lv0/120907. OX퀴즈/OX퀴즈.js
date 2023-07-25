function solution(quiz) {
    var answer = [];
    for (let i = 0; i < quiz.length; i++){
        const q = quiz[i].split("=")
        let front = Number(eval(q[0]))
        if (front == q[1]){
            answer.push("O")
        } else {
            answer.push("X")
        }
    }
    return answer;
}