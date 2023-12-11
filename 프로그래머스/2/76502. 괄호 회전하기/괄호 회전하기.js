function solution(s) {
    s = s.split('')
    sLen = s.length
    let answer = 0;
    
    const isValid = (word) => {
        let words = [...word]
        let vaild = true
        let stack = []
        while (words.length > 0){
            const wpop = words.shift()
            if (stack.length === 0){
              stack.push(wpop)  
            } else if (wpop === ']' && stack[stack.length -1] === '['){
                stack.pop()
            } else if (wpop === '}' && stack[stack.length -1] === '{'){
                stack.pop()
            } else if (wpop === ')' && stack[stack.length -1] === '('){
                stack.pop()
            } else {
                stack.push(wpop)
            }
        }
        if (stack.length > 0){
            valid = false
        } else {
            valid = true
        }
        return valid
    }
    
    for (let i = 0; i < sLen; i++){
        const spopLeft = s.shift()
        s.push(spopLeft)
        if (isValid(s)) {answer += 1}
    }
    
    return answer;
}