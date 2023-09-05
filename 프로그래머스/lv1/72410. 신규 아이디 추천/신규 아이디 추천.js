function solution(new_id) {
    // 1단계
    new_id = new_id.toLowerCase()
    // 2단계
    const eng = /[a-z]/; //영어
    const num = /[0-9]/ // 숫자
    const mark = /[-_.]/ // 기호
    for (n of new_id){
        if (!eng.test(n) && !num.test(n) && !mark.test(n)){
            new_id = new_id.replace(n, '')
        }
    }
    // 3단계
    let real_new = []
    for (n of new_id){
        if (n == "."){
            if (real_new[real_new.length-1] != '.'){
                real_new.push(n)
            }
        } else {
            real_new.push(n)
        }
    }
    // 4단계
    if (real_new[0] == "."){
        real_new = real_new.slice(1)
    }
    if(real_new[real_new.length-1] == "."){
        real_new = real_new.slice(0, -1)
    }
    // 5단계
    if (real_new.length == 0){
        real_new.push('a')
    }
    // 6단계
    if (real_new.length >= 16){
        real_new = real_new.slice(0, 15)
    }
    if(real_new[real_new.length-1] == "."){
        real_new = real_new.slice(0, -1)
    }
    // 7단계
    if (real_new.length <= 2){
        let last = real_new[real_new.length-1]
        while(real_new.length < 3){
            real_new.push(last)        
        }
    }
    return real_new.join('');
}