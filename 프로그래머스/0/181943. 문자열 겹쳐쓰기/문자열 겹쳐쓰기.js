function solution(my_string, overwrite_string, s) {
    const length = overwrite_string.length
    console.log( my_string.slice(0, s), my_string.slice(s + length, my_string.length))
    my_string = my_string.slice(0, s) + overwrite_string + my_string.slice(s + length, my_string.length)
    return my_string;
}