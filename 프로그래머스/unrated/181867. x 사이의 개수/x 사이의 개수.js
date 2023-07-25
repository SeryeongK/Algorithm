function solution(myString) {
    var answer = [];
    answer = myString.split("x")
    for (let i = 0; i < answer.length; i++){
        answer[i] = answer[i].length
    }
    return answer;
}