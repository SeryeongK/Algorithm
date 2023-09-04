function solution(id_list, report, k) {
    const set = new Set(report);
    const uniqueArr = [...set];
    let warn = {} // 신고당한 횟수
    let result = {} 
    let reporters = {} // 신고당한 사람 : Set(신고자)
    for (i of id_list){
        warn[i] = 0
        result[i] = 0
        reporters[i] = new Set()
    }
    // 경고 누적 횟수
    for (u of uniqueArr){
        let now = u.split(" ")
        let sad = now[1]
        warn[sad] ++
        let angry = now[0]
        reporters[sad].add(angry)
    }
    // 경고에 따라 결과 정리
    for (let w in warn){
        if (warn[w] >= k){
            let rps = reporters[w]
            for (rp of rps){
                result[rp] ++
            }
        }
    }
    return Object.values(result);
}