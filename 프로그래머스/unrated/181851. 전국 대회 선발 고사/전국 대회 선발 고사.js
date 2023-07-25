function solution(rank, attendance) {
    for (let i = 0; i < rank.length; i++){
        if (!attendance[i]){
            rank[i] = 0
        }
    }
    const copy = JSON.parse(JSON.stringify(rank))
    rank = rank.filter(function(data) {return data > 0})
    rank.sort(function (a, b){
        return a - b
    })
    const one = copy.indexOf(rank[0])
    const two = copy.indexOf(rank[1])
    const three = copy.indexOf(rank[2])
    var answer = 10000 * one + 100 * two + three;
    return answer;
}