function solution(price, money, count) {
    let total = 0
    for (let i = 1; i <= count; i++){
        total += (price*i)
    }
    let answer = money - total
    if (answer >= 0){
        answer = 0
    } else {
        answer = Math.abs(answer)
    }
    return answer;
}