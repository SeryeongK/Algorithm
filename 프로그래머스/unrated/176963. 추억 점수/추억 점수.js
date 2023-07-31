function solution(name, yearning, photo) {
    let score = {}
    for (let i = 0; i < name.length; i++){
        score[name[i]] = yearning[i]
    }
    var answer = [];
    photo.map((pho) => {
        let number = 0
        pho.map((per) => {
            if (score[per]){
            number += score[per]
            }
        })
        answer.push(number)
    })
    return answer;
}