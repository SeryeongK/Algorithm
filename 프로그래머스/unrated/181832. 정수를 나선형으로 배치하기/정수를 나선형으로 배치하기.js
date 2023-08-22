function solution(n) {
    let N = n
    n--
let mat = new Array(N);
for (let i = 0; i < N; i++) {
    mat[i] = new Array(N).fill(0);
}
    let [dir , x, y] = [0, 0, 0]
    let cnt = 0
    for (let i =1; i<=(N*N); i++){
        console.log(x, y, dir, n, i, cnt)
        mat[y][x] = i

        if (dir == 0){ // 오른쪽
            if (x == n){
                dir = 1
                y++
            }else {
            x ++}
        } else if (dir == 1){ // 아래쪽
            if( y ==n){
                dir = 2
                x--
            }else{
            y++}
        }else if (dir == 2) { // 왼쪽
            if(x ==cnt ){
                dir = 3
                n--
                cnt ++
                y--
            }else {
            x--}
        } else{ // 위쪽
            if(y == cnt && y == cnt){
                dir  = 0
                x++
            }else {
            y--
            }
        }
        
    }
    console.log(mat)
    return mat;
}