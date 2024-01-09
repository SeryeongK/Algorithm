// function solution(number, limit, power) {
//     let answer = 0;
//     let DP = [1]
//     for (let i = 1; i < number; i++){
//         DP.push(0)
//     }
//     for (let i = 2; i <= number; i++){
//         if (DP[i-1] === 0){
//             let num = 2
//             for (let j = 2; j < i; j++){
//                 if (i % j === 0){
//                     num += 1
//                 }
//             }
//             console.log(i-1)
//             DP[i-1] = num
//             if (i * 2 < number){
//                 if ( DP[i *2-1] === 0){
//                     DP[i *2-1] = num +1    
//                 } else {
//                     DP[i *2-1] += 1
//                 } 
//             } 
//             if (i * 3 < number){
//                 if ( DP[i *3-1] === 0){
//                     DP[i *3-1] = num +1    
//                 } else {
//                     DP[i *3-1] += 1
//                 } 
//             } 
//         } 
//     }
//     console.log(DP)
//     for (dp of DP){
//         if (dp > limit){
//             answer += power
//         } else {
//             answer += dp
//         }
//     }
//     return answer;
// }

function solution(number, limit, power) {
    let answer = 0;
    let tempArr = [];

    // 1)
    for(let i=1; i<=number; i++) {
        tempArr.push(divisor(i))
    }

    // 2)
    tempArr.forEach((e, i) => {
        if(e > limit) {
            tempArr[i] = power
        }
    })

    // 3)
    tempArr.forEach((e, i) => {
        answer += e;
    })

    return answer;
}

// 약수 개수 구하기
// 시간복잡도 생각하기
function divisor(num) {
    let count = 0;

    // num = 9
    // 1, 3, 3, 9
    for(let i=1; i<=Math.sqrt(num); i++) {
        // 3 약수 중복 방지
        if(i === Math.sqrt(num)) {
            count += 1;
        } 
        // 1, 9
        else if(num % i == 0) {
            count += 2;
        }
    }
    return count;
}
