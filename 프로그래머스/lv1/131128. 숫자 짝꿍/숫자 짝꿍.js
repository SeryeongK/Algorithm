function solution(X, Y) {
    let nums1 = {}
    for (x of X){
        if (nums1[x]){
            nums1[x] ++
        }else {
            nums1[x] = 1
        }
    }
    let nums2 = {}
    for (y of Y){
        if (nums2[y]){
            nums2[y] ++
        }else {
            nums2[y] = 1
        }
    }
    
    let result = []
    for (let i = 0; i <= 9; i++){
        let min = Math.min(nums1[i], nums2[i])
        if (min > 0){
            for (let j = 0; j < min; j++){
                result.push(i)
            }
        }
    }
    var answer = '';
    if (result.length == 0){
        answer = '-1'
    }else{
        result.sort((a, b) => {return b -a})
        answer = result.join("")
    }

    if (answer.split("").filter(element => element != "0").length == 0){
        answer = "0"
    }
    
    return answer;
}