function solution(array) {
    let nums = []

    for (let i =0; i < array.length; i++){
        let now = array[i]
        let cnt = 0
        for (let j = 0; j < array.length; j++){
            if (now == array[j]){
                cnt++
                array[j] = -3
            }
        }
        nums.push([now, cnt])
        }
    nums = nums.filter(e => e[0] != -3)
nums.sort((a, b) => {
    return b[1] - a[1]
})
     let answer = nums[0]
    for (let i = 1; i < nums.length; i++){
        if(answer[1] > nums[i][1]){
            break
        }
        else if(nums[i][1] == answer[1]){
            answer = -1
            break
        } 
    }
    if (answer != -1){
        answer = answer[0]
    }
    return answer;
}