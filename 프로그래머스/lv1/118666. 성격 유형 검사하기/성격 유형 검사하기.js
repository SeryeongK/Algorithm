function solution(survey, choices) {
    let table = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for (let i = 0; i < survey.length; i++){
        let nowc = choices[i]
        let nows = survey[i].split("")
        if (nowc == 1){
            table[nows[0]] = table[nows[0]] + 3
        } else if (nowc == 2){
            table[nows[0]] = table[nows[0]] + 2
        } else if (nowc == 3){
            table[nows[0]] ++
        } else if (nowc == 5){
            table[nows[1]] ++
        } else if (nowc == 6){
            table[nows[1]] = table[nows[1]] + 2
        } else if (nowc == 7){
            table[nows[1]] = table[nows[1]] + 3
        }
    }
    // 점수 계산
    var answer = [];
    table["R"] >= table["T"] ? answer.push("R") : answer.push("T")
    table["C"] >= table["F"]?answer.push("C"):answer.push("F")
    table["J"] >= table["M"]?answer.push("J") : answer.push("M") 
    table["A"] >= table["N"] ? answer.push("A"): answer.push("N")
    return answer.join("");
}