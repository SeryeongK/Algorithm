function solution(n, arr1, arr2) {
    let answer = [];
    let arrOne = []
    let arrTwo = []
    let combine = []
    const binary = (num) => {
        let result = []
        while(num > 1){
            result.push(num % 2)
            num = Math.floor(num / 2)
        }
        result.push(num)
        while (result.length < n){
            result.push(0)
        }
        return result.reverse()
    }
    for (a of arr1){
        arrOne.push(binary(a))
    }
    for (a of arr2){
        arrTwo.push(binary(a))
    }
    for (let i = 0; i < n; i++){
        let temp = ""
        for (let j = 0; j < n; j++){
            const result = arrOne[i][j] || arrTwo[i][j]
            if (result){
                temp += "#"
            } else {
                temp += " "
            }
        }
        answer.push(temp)
    }
    return answer;
}