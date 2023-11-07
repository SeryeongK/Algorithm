function solution(sizes) {
    let m = [0, 0]
    for (s of sizes){
        s = s.sort((a, b) => {return a - b})
        if (s[0] >= m[0]) {
            m[0] = s[0]
        }
        if (s[1] >= m[1]) {
            m[1] = s[1]
        }
    }
    return m[0] * m[1];
}