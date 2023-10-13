function solution(s){
    var answer = true;
    let temp = []
    if (s[0] == ")" || s[s.length-1] == "("){
        answer = false
    } else {
        for (bracket of s){
            if (bracket == "("){
                temp.push(bracket)
            } else if (bracket == ")" && temp[temp.length-1] == "("){
                temp.pop()
            } else {
                answer = false
                break
            }
        }    
    }
    
    if (temp.length > 0){
        answer = false
    }

    return answer;
}