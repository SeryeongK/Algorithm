function solution(s){
    s = s.toLowerCase()
    let p = 0
    let y = 0
    for (word of s){
        if (word == "p"){
            p++
        } else if (word == "y"){
            y++
        }
    }
    
    let answer = false
    if (p == y){
        answer = true
    }
    
    return answer;
}