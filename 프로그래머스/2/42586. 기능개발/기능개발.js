function solution(progresses, speeds) {
    let answer = [];
    let days = []
    for (let i = 0; i < progresses.length; i++){
        days.push(Math.ceil((100 - progresses[i]) / speeds[i])) 
    }
    if ( days.length > 0){
        for (let i = 1; i < days.length; i++){
            if (days[i] < days[i-1]){
                days[i] = days[i-1]
            }
        }    
    }    
    days.sort((a, b) => a - b)
    let cnt = 1
    let day = days[0]
    if (days.length > 0)
    for (let i = 1; i <= days.length; i++){
        if (days[i] === day){
            cnt += 1
        } else {
            day = days[i]
            answer.push(cnt)
            cnt = 1
        }
    }
    return answer;
}