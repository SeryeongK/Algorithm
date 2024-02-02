function solution(common) {
    let answer = 0;
    // 등차수열이면
    if ((common[0]-common[1]) === (common[1]-common[2])){
        if (common[0] > common[1]){
            answer = common[common.length-1] - (common[0]-common[1])
        } else {
            answer = common[common.length-1] + (common[1]-common[0])
        }
    } else { // 등비수열이면
        if(common[0] > common[1]){
            answer = common[common.length-1] / (common[0] / common[1])    
        } else {
            answer = common[common.length-1] * (common[1] / common[0])    
        }
    }
    return answer;
}