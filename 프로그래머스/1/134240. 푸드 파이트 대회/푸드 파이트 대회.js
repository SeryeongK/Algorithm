function solution(food) {
    let answer = '';
    for (let i = 1; i < food.length; i++){
        if (food[i] % 2 === 0){
            for (let j = 0; j < food[i] / 2; j++){
                answer += i
            }
        } else if ((food[i] / 2) > 1){
            for (let j = 0; j < (food[i]-1)/2; j++){
                answer += i
            }
        }
    }
    return answer+'0'+answer.split("").reverse().join("");
}