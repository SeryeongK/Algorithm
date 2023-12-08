function solution(k, tangerine) {
    let answer = 0;
    let tangerines = {}
    for (t of tangerine){
        if (tangerines[t] !== undefined){
            tangerines[t] += 1
        } else {
            tangerines[t] = 1
        }
    }
    let tans = []
    for (const t in tangerines){
        tans.push([t, tangerines[t]])
    }
    tans.sort((a, b) => a[1] - b[1])
    while (k > 0){
        k -= tans.pop()[1]
        answer += 1
    }
    return answer;
}