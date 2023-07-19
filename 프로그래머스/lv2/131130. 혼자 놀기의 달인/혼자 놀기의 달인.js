function solution(cards) {
    let [result, group] = [[], []]
    let visited = Array(cards.length).fill(0)
    let idx = 0
    while (1) {
        if (visited.indexOf(0) == -1){ // 모두 다 방문한 경우
            result.push(group.length)
            break
        }else if (!visited[idx]) {// 새로운 곳을 방문한 경우
            visited[idx] = 1
            group.push(cards[idx])
            idx = cards[idx] -1
        }else { // 이미 방문한 곳을 방문한 경우(한 그룹의 끝)
            result.push(group.length)
            group = []
            idx = visited.indexOf(0)
        }
    }
    result.sort(function(a, b){
        return b - a
    })
    var answer = 0
    // 그룹이 하나일 경우
    if(result.length == 1){
        answer = 0
    } else {
        answer = result[0] * result[1]
    };
    return answer;
}