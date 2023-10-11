function solution(s) {
    let alpha = {}
    let result = []
    for (let i = 0; i < s.length; i++){
        let location = alpha[s[i]]
        if (location == undefined){
            result.push(-1)
        } else {
            result.push(i - location)            
        }
        alpha[s[i]] = i
    }
    return result;
}