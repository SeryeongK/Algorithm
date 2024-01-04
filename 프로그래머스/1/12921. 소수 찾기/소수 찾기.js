function solution(n) {
    let answer = 0;
    let nums = [0, 0, 1]
    for (let i = 3; i < n + 1; i++){
        nums.push(1)
    }
    for (let i = 2; i < Math.floor(Math.sqrt(n))+1; i++){
        if (nums[i]){
            let j = 2
            while (i * j <= n){
                nums[i * j] = 0
                j += 1
            }
        }
    }
    for (n of nums){
        if (n){
            answer += 1
        }
    }
    return answer;
}