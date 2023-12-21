function solution(cards1, cards2, goal) {
    let answer = "Yes";
    let one = []
    let two = []
    for (g of goal) {
        if (cards1.includes(g)){
            one.push(cards1.indexOf(g))
        } else {
            two.push(cards2.indexOf(g))
        }
    }
    
    let strOne = JSON.stringify(one)
    let strTwo = JSON.stringify(two)
    let sortedOne = one.sort((a, b) => a - b)
    let sortedTwo = two.sort((a, b) => a - b)
    if (strOne !== JSON.stringify(sortedOne) || strTwo !== JSON.stringify(sortedTwo)){
        answer = "No"
    }
    if (sortedOne.length > 1){
        for (let i = 1; i < sortedOne.length; i++){
            if (sortedOne[i] > sortedOne[i-1]+1){
                answer = "No"
                break
            }
        }    
    }
    if (sortedTwo.length > 1){
        for (let i = 1; i < sortedTwo.length; i++){
            if (sortedTwo[i] > sortedTwo[i-1]+1){
                answer = "No"
                break
            }
        }    
    }
    
    return answer;
}