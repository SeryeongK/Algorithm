function solution(board) {
    const dx = [0, 1, 0, -1, -1, 1, -1, 1]
    const dy = [-1, 0, 1, 0, -1, -1, 1, 1]
    const N = board[0].length
    let cnt = N*N
    for (let i = 0; i< N; i++){
        for (let j = 0; j< N; j++){
        let now = board[i][j]
        if(now == 1){
            cnt--
            for(let d = 0; d <= 7; d++){
                let tempx = i+dx[d]
                let tempy = j+dy[d]
                if (0<=tempx && tempx<N && 0<=tempy && tempy<N){
                    if(board[tempx][tempy] == 0){
                        board[tempx][tempy] = 2
                        cnt--
                    }
                }
            }
        }
        }
    }
    return cnt;
}