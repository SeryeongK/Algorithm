function solution(s) {
    let upper = []
    let lower = []
    for (str of s){
        if (str === str.toUpperCase()){
            upper.push(str)
        } else {
            lower.push(str)
        }
    }
    upper = upper.sort((a, b) => b.localeCompare(a))
    lower = lower.sort((a, b) => b.localeCompare(a))
    return lower.join("")+upper.join("");
}