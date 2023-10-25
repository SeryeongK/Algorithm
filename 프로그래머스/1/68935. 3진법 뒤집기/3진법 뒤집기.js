function solution(n) {
    var answer = 0;
    let decimalThree = []
    while(n / 3 > 0){
        decimalThree.push(n % 3)
        n = Math.floor(n / 3)
    }
    let decimalTen = 0
    for(let i = 0; i < decimalThree.length; i++){
        decimalTen += (3 ** (decimalThree.length -i -1) * decimalThree[i])
    }
    return decimalTen;
}