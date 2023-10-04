def solution(s):
    s = s.split(" ")
    nums = list(map(int, s))
    nums.sort()
    answer = str(nums[0]) + " " + str(nums[-1])
    return answer