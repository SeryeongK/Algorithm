function solution(arr, delete_list) {
    
    var answer = arr.filter(function(data) {
        return !delete_list.includes(data)
    })
    return answer;
}