function solution(numbers) {
    const ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    let answer = 0;
    for (t of ten){
        if (!numbers.includes(t)){
            answer += t
        }
    }
    return answer;
}