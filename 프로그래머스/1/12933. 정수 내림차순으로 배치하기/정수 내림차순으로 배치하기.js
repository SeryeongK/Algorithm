function solution(n) {
    n = String(n).split("")
    n = n.map((e) => {return Number(e)})
    n.sort((a, b) => b - a)
    return Number(n.join(""));
}