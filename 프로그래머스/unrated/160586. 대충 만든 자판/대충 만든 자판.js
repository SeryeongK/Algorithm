function solution(keymap, targets) {
    let alpha = {}
    // 각각의 알파벳 최소 위치 저장
    for (k of keymap){
        for (let i = 0; i < k.length; i++){
            if(alpha[k[i]]){
                if (alpha[k[i]] > i){
                    alpha[k[i]] = i + 1
                }
            }else {
                alpha[k[i]] = i + 1
            }
        }
    }
    // 타겟 번호 찾기
    var answer = [];
    for (t of targets){
        let cnt = 0
        let valid = 0
        for (let i = 0; i<t.length; i++){
            if (alpha[t[i]]){
                cnt = alpha[t[i]] + cnt                
            }else {
                valid --
            }
        }
        if(cnt > 0){
            answer.push(cnt)                
        }
        if (valid < 0){
            if (cnt > 0){
                answer.pop()
            }
            answer.push(-1)
        }
    }
    return answer;
}