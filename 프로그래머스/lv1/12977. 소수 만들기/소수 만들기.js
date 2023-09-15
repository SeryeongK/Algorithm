function solution(nums) {
    let answer = 0;
    // 소수 구해두기
    nums = nums.sort((a, b) =>  a-b)
    let m = nums[nums.length-1] + nums[nums.length-2] + nums[nums.length-3]
    let prime = []
    for (let i = nums[0]; i <= m; i++){
        let cnt = 0
        for (let j = 2; j < i; j++){
            if (i % j == 0){
                cnt++
                break
            }
        }
        if (cnt == 0){
            prime.push(i)
        }
    }
    // nums 판별하기
    for (let i = 0; i < nums.length-2; i++){
        for (let j = i+1; j < nums.length-1; j++){
            for (let k = j+1; k <nums.length; k++){
                if (prime.includes(nums[i]+nums[j]+nums[k])){
                    answer++
                }
            }
        }
    }
    return answer;
}