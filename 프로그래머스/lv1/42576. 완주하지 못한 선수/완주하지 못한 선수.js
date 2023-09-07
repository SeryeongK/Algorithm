function solution(participant, completion) {
    let answer = ""
    let completiondic = {}
    for (p of participant){
        completiondic[p] = 0
    }
    for (c of completion){
        completiondic[c] ++
    }
    for (p of participant){
        if (completiondic[p] > 0){
            completiondic[p] --
        }else {
            answer = p
        }        
    }
    return answer;
}