function solution(n) {
    var answer = 0;
    const isComp = (number) => {
        let divisor = 0
        for (let i = 2; i < number; i++){
            if (number % i === 0){
                divisor += 1
                break
            }
        }
        if (divisor){
            return true
        } else {
            return false
        }
    }
    let compList = []
    if (n > 3){
        for (let i = 4; i <= n; i++){
            if (!compList.includes(i) && isComp(i)) {
                answer += 1
                compList.push(i)
                let step = 2
                let mul = i 
                while (mul * step <= n){
                    if (!compList.includes(mul * step)){
                        compList.push(mul * step)
                        answer += 1
                    }
                    step += 1
                }
            }
        }
    }
    return answer;
}