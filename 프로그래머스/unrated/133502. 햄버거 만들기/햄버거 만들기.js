function solution(ingredient) {
    let left = []
    let hamburger = []
    let order = [ 1, 2, 3, 1 ]
    let idx = 0
    let result = 0
    let cnt = 0
    let now = 0
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