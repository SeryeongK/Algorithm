function solution(wallpaper) {
    let minx = 100
    let miny = 100
    let maxx = 0
    let maxy = 0
    for (let i = 0; i < wallpaper.length; i++){
        for (let j = 0; j<wallpaper[0].length; j++){
            if (wallpaper[i][j] == "#"){
                if (i < minx){
                    minx = i
                }
                if (j < miny){
                    miny = j
                }
                if (i > maxx){
                    maxx = i
                }
                if (j > maxy){
                    maxy = j
                }
            }
        }
    }
    return [minx, miny, maxx+1, maxy+1];
}