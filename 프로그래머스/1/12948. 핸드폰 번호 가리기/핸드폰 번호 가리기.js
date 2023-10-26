function solution(phone_number) {
    var answer = '';
    let back = phone_number.slice(-4, phone_number.length)
    let front = phone_number.slice(0, -4)
    answer = ('*'.repeat(front.length)) + back
    return answer;
}