function solution(park, routes) {
    const dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    let start = []
    for (let i = 0; i<park.length; i++){
        let p = park[i]
        for (let j = 0; j<park[0].length; j++){
            if (p[j] == "S"){
                start = [i, j]
                break
            }
        }
    }
    for (r of routes){
        r = r.split(" ")
        let d = r[0]
        let l = Number(r[1])
        if (d == "N"){
            d = dir[0]}
        else if (d == "E"){
            d = dir[1]}
        else if (d == "S"){
            d = dir[2]}
        else{
            d = dir[3]
        }
        let bomb = 0
        let temp = start
        for (let i = 0; i < l; i++){
            temp = [temp[0]+d[0], temp[1]+d[1]]
            if (0 > temp[0] || temp[0] >=park.length || 0 > temp[1] || temp[1] >=park[0].length){
                bomb ++
                break
            }
            else if (park[temp[0]][temp[1]] == "X"){
                 bomb ++
                break
             }
        }
        if (bomb == 0){
            start = temp
        }
    }
        return start;
}