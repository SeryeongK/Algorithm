function solution(nums) {
    let answer = 0;
    let maxNum = nums.length /2
    let pocketmon = [...new Set(nums)].length
    if (maxNum >= pocketmon){
        answer = pocketmon
    } else {
        answer = maxNum
    }
    return answer;
}