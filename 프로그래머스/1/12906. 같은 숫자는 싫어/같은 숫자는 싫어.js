function solution(arr)
{
    var answer = [];
    for (num of arr){
        if (answer.length == 0 || answer[answer.length-1] != num){
            answer.push(num)
        }
    }
    return answer;
}