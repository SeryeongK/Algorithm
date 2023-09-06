function solution(ingredient) {
    let hamburger = []
    let result = 0
    for (let i = 0; i <ingredient.length; i++) {
        hamburger.push(ingredient[i])
        let temp = hamburger.slice(-4)
        if (temp[0] == 1 && temp[1] == 2 && temp[2] == 3 && temp[3] == 1){
            for (let j = 0; j < 4; j++){
                hamburger.pop()                
            }
            result ++
        }
    }
    return result;
}