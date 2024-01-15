// function solution(phone_book) {
//     let answer = true;
//     phone_book = phone_book.sort((a, b) => a - b)
//     for (let i = 0; i< phone_book.length; i++){
//         for (let j = i+1; j < phone_book.length; j++){
//             const compareA = phone_book[i]
//             if (compareA === phone_book[j].slice(0, compareA.length)){
//                 answer = false
//                 break;
//             }
//         }
//         if (answer === false){
//             break
//         }
//     }
//     return answer;
// }

function solution(phone_book) {
    let answer = true;
    let hashMap = {};

    // 해시맵에 전화번호를 저장
    for (let i = 0; i < phone_book.length; i++) {
        hashMap[phone_book[i]] = true;
    }

    // 각 전화번호의 부분 문자열이 해시맵에 있는지 확인
    for (let i = 0; i < phone_book.length; i++) {
        for (let j = 1; j < phone_book[i].length; j++) {
            const prefix = phone_book[i].slice(0, j);
            if (hashMap[prefix]) {
                answer = false;
                break;
            }
        }
        if (!answer) {
            break;
        }
    }

    return answer;
}