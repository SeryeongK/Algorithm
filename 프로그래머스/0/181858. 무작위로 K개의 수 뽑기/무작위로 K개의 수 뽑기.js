function solution(arr, k) {
    var answer = [];
    for (a of arr){
         if (answer.length >= k){
            break
        }
        if (!answer.includes(a)){
            answer.push(a)
        }
    }
    while(answer.length < k){
        answer.push(-1)
    }
    return answer;
}