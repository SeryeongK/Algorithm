function solution(numbers, hand) {
    const kepad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    let result = []
    let [lx, ly] = [3, 0]
    let [rx, ry] = [3, 2]
    let [templ, tempr] = [0, 0]
    for (n of numbers){
        switch (n){
            // 왼손
            case 1:
                result.push("L")
                lx = 0
                ly = 0
                break
            case 4:
                result.push("L")
                lx = 1
                ly = 0
                break
            case 7:
                result.push("L")
                lx = 2
                ly = 0
                break
            // 오른손
            case 3:
                result.push("R")
                rx = 0
                ry = 2
                break
            case 6:
                result.push("R")
                rx = 1
                ry = 2
                break
            case 9:
                result.push("R")
                rx = 2
                ry = 2
                break
            // 양손
            case 2:
                templ = Math.abs(0-lx) + Math.abs(1-ly)
                tempr = Math.abs(0-rx) + Math.abs(1-ry)
                if (templ < tempr || (templ == tempr && hand == "left")){
                    result.push("L")
                    lx = 0
                    ly = 1
                } else if (templ > tempr|| (templ == tempr && hand == "right")){
                    result.push("R")
                    rx = 0
                    ry = 1
                }
                break
            case 5:
                templ = Math.abs(1-lx) + Math.abs(1-ly)
                tempr = Math.abs(1-rx) + Math.abs(1-ry)
                if (templ < tempr || (templ == tempr && hand == "left")){
                    result.push("L")
                    lx = 1
                    ly = 1
                } else if (templ > tempr|| (templ == tempr && hand == "right")){
                    result.push("R")
                    rx = 1
                    ry = 1
                }
                break
            case 8:
                templ = Math.abs(2-lx) + Math.abs(1-ly)
                tempr = Math.abs(2-rx) + Math.abs(1-ry)
                if (templ < tempr || (templ == tempr && hand == "left")){
                    result.push("L")
                    lx = 2
                    ly = 1
                } else if (templ > tempr|| (templ == tempr && hand == "right")){
                    result.push("R")
                    rx = 2
                    ry = 1
                }
                break
            case 0:
                templ = Math.abs(3-lx) + Math.abs(1-ly)
                tempr = Math.abs(3-rx) + Math.abs(1-ry)
                if (templ < tempr || (templ == tempr && hand == "left")){
                    result.push("L")
                    lx = 3
                    ly = 1
                } else if (templ > tempr|| (templ == tempr && hand == "right")){
                    result.push("R")
                    rx = 3
                    ry = 1
                }
                break
        }
    }
    return result.join("");
}