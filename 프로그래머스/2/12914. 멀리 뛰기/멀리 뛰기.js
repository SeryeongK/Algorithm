// 규칙이 있다 -> DP 생각해보기
function solution(n) {
    let DP = [1, 2]
    for (let i = 2; i < n; i++){
        DP[i] = (DP[i-1] + DP[i-2]) % 1234567
    }
    return DP[n-1];
}