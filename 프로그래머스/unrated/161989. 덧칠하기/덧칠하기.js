function solution(n, m, section) {
    var answer = 0;
    let paint = section[0] -1
    for (s of section){
        if (paint< s){
            paint = s + (m-1)
            answer ++
        }
    }
    return answer;
}