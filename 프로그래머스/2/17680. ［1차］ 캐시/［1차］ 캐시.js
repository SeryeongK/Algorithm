function solution(cacheSize, cities) {
    var answer = 0;
    let cache = []
    if (cacheSize === 0){
        return cities.length * 5
    }
    for (c of cities){
        c = c.toLowerCase()
        if (cache.includes(c)){
            answer += 1
            cache = cache.filter((e) => e !== c)
        } else {
            answer += 5
            if (cache.length === cacheSize){
                cache.shift()
            }
        }
        cache.push(c)
    }
    return answer;
}