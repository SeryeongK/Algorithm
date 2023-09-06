function solution(board, moves) {
    var answer = 0;
    let line = {}
    for (b of board){
        for (let i = 0; i < b.length; i++){
            line[i+1] = []
        }   
    }
    for (b of board){
        for (let i = 0; i < b.length; i++){
            if(b[i]){
                line[i+1].push(b[i])                
            }
        }
    }
    // 아이템 쌓기
    let stack = []
    let pop = 0
    for (m of moves){
        let last = 0
        if (stack.length > 0){
            last = stack.pop()
        }
        if (last == line[m][0]){
            pop += 2
        } else {
            stack.push(last)
            line[m][0] && stack.push(line[m][0])            
        }
        line[m][0] && line[m].shift()
    }
    return pop;
}