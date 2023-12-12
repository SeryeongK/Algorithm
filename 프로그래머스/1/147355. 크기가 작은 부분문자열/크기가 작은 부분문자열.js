function solution(t, p) {
    let answer = 0;
    for (let i = 0; i < t.length -p.length +1; i++){
        const temp = Number(t.split("").splice(i, p.length).join(""))
        if (Number(p) >= temp){
            answer += 1
        }
    }
    return answer;
}