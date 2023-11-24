function solution(s) {
    let answer = [];
    s = s.slice(2, s.length-2).split("},{")
    let numbers = {}
    for (nums of s){
        nums = nums.split(",")
        numbers[nums.length] = nums.map(e => Number(e))
    }
    for (let i = 1; i <= s.length; i++){
        const now = numbers[i]
        for (n of now){
            if (!answer.includes(n)){
                answer.push(n)
            }
        }
    }
    return answer;
}