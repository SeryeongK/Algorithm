function solution(s) {
    s = s.split('')
    real = [...s]
    for (let i = 0; i <= s.length; i++){
        let count = 0;
        let now = s[i]
        console.log(now)
       for (let j = 0; j <= s.length; j++){
          if(s[j] == now){
              count++
          }
       }
        if (count >=2){
            real = real.filter((e) => e != now)
        }
    }
    real = real.sort()
    answer = real.join("")
    return answer;
}