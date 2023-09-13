function solution(n)
{
    let answer = 0
    n = String(n).split('').map(n => Number(n))
    for (num of n){
        answer += num
    }
    return answer;
}