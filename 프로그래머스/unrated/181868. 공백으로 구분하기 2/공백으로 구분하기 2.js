function solution(my_string) {
    var answer = [];
    answer = my_string.split(" ")
    answer = answer.filter(s => s.length >= 1)
    return answer;
}