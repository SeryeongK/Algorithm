input = int(input())

if input < 100:
    print(input)
elif 1000 > input >= 100:
    cnt = 99
    for i in range(100, input+1):
        nums = list(map(int, list(str(i))))
        if (nums[2] - nums[1]) == (nums[1] - nums[0]):
            cnt += 1
    print(cnt)
elif input == 1000:
    print(144)