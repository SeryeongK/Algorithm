// function solution(priorities, location) {
//     let numbers = []
//     for (let i = 0; i < priorities.length; i++){
//         numbers.push([priorities[i], i])
//     }
//     priorities.sort((a, b) => b - a)

//     let result = {}
//     let priority = 1
//     while (priority !== priorities.length+1){
//         const num = numbers[0][0]
//         const loc = numbers[0][1]
//         // 현재 최고 우선순위이면
//         if (num === priorities[0]){
//             result[loc] = priority
//             priority += 1
//             priorities = priorities.shift()
//         }
//         // 현재 최고 우선순위가 아니면
//         const end = numbers.shift()
//         numbers.push(end)
//     }
//     console.log(result)
//     return result[location];
// }

// 다 비교해서 저장할 필요가 없음
function solution(priorities, location) {
    const queue = priorities.map((priority, index) => ({ priority, index }));
    let result = 0;

    while (queue.length > 0) {
        const current = queue.shift();
        if (queue.some(item => item.priority > current.priority)) {
            queue.push(current);
        } else {
            result++;
            if (current.index === location) {
                break;
            }
        }
    }

    return result;
}
