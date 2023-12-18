function solution(arr1, arr2) {
    let answer = [];
    for (let i = 0; i < arr1.length; i++){
        let temp = []
        for (let j = 0; j < arr1[0].length; j++){
            temp.push(Number(arr1[i][j]) + Number(arr2[i][j]))
        }
        answer.push(temp)
    }
    return answer;
}