function solution(numbers) {
    let numSet = []
    for (let i = 0; i < numbers.length-1; i++){
        for (let j = i+1; j < numbers.length; j++){
            numSet.push(numbers[i]+numbers[j])
        }
    }
    numSet = new Set(numSet)
    numSet = [...numSet]
    numSet.sort((a, b) => {return a - b})
    return numSet;
}