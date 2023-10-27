function solution(x) {
    var answer = true;
    let sumx = 0
    x = String(x)
    for(let i = 0; i < x.length; i++){
        sumx += Number(x[i])
    }    
    if (Number(x) % sumx != 0){
        answer = false
    }
    return answer;
}