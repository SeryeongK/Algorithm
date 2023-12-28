function solution(s, n) {
    let answer = [];
    const alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    s = s.split("")
    for (letter of s){
        let low = true
        if (letter !== letter.toLowerCase()){
            low = false
        }
        if (low && alpha.indexOf(letter) === -1){
            answer.push(' ')
            continue
        }
        let idx = alpha.indexOf(letter.toLowerCase()) + n
        if (idx > 25) {
            idx -= 26
        }
        if (low){
            answer.push(alpha[idx])
        } else {
            answer.push(alpha[idx].toUpperCase())
        }
    }
    return answer.join("");
}