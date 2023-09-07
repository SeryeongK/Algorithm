function solution(n, lost, reserve) {
    var answer = n - lost.length
    lost = lost.sort()
    reserve = reserve.sort()
    for (l of lost){
        if (reserve.includes(l)){
            delete reserve[reserve.indexOf(l)]
            delete lost[lost.indexOf(l)]
            answer++
        }
    }
    for (l of lost){
        let [front, back] = [0, 0]
        if (l){
            front = l-1
            back = l+1
        }
        if (reserve.includes(front)){
            delete reserve[reserve.indexOf(front)]
            answer ++   
        } else if (reserve.includes(back)){
            delete reserve[reserve.indexOf(back)]
            answer ++
        }
        if(reserve.length == 0){
            break
        }
    }
    return answer;
}