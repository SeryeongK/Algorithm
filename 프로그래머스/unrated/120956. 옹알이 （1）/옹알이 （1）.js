function solution(babbling) {
    var answer = 0;
    for (b of babbling){
        while (b.length > 0){
            let isShifted = false
            if (b.slice(0, 3) == "aya" || b.slice(0, 3) == "woo"){
                b = b.slice(3)
                isShifted = true
            } else if (b.slice(0, 2) == "ye" || b.slice(0, 2) == "ma"){
                b = b.slice(2)
                isShifted = true
            } else {
                break
            }
            if (!isShifted){
                break
            }
        }
        if (b.length == 0){
            answer += 1
        }
    }
    return answer;
}