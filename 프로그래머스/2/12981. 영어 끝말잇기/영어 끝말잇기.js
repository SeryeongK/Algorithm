function solution(n, words) {
    let answer = [];
    let result = []
    for (let i = 0; i < words.length; i++){
        const now = words[i]
        if (now.length < 2){
            result = [i % n + 1, Math.ceil((i+1) / n)]
            break
        }
       if (i > 0){
           const last = answer[answer.length-1]
           if (last[last.length-1] !== now[0]){
               result = [i % n + 1, Math.ceil((i+1) / n)]
               break
           }
       } 
        if(answer.includes(now)){
            result = [i % n + 1, Math.ceil((i+1) / n)]
            break
        }
        answer.push(now)
    }

    if (result.length == 0){
        result = [0, 0]
    }
    
    return result;
}