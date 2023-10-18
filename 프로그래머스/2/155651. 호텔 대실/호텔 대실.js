function solution(book_time) {   
    const changeTime = (time) => {
        time = time.split(":")
        return Number(time[0] * 60) + Number(time[1])
    }
    
    let bookTime = []
    for(t of book_time){
        const start = changeTime(t[0])
        const end = changeTime(t[1]) + 10
        const gap = changeTime(t[1]) - changeTime(t[0])
        bookTime.push([start, end, gap])
    }
    bookTime.sort(function(a, b) {
        if (a[0] < b[0]){
            return -1; // a가 b보다 작음
        } else if (a[0] > b[0]){
            return 1; // a가 b보다 큼
        } else {
            if (a[2] < b[2]){
                return -1; // a가 b보다 작음
            } else if (a[2] > b[2]){
                return 1; // a가 b보다 큼
            } else {
                return 0; // 같음
            }
        }
    });

    let rooms = []
    for (t of bookTime) {
        if (rooms.length > 0){
            if (rooms[0] <= t[0]){
                rooms[0] = t[1]
            } else {
                rooms.push(t[1])
            }
        } else {
            rooms.push(t[1])
        }
        rooms.sort((a, b) => a - b)
    }
    return rooms.length;
}