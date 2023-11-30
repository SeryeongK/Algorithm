function solution(n) {
    let DP = [0, 1]
    for (let i = 2; i <= n; i++){
        DP.push((DP[i-1] + DP[i-2]) % 1234567)
    }
    return DP[n];
}