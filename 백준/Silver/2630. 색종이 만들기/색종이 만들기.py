import sys

N = int(sys.stdin.readline())
colors = [sys.stdin.readline().split() for _ in range(N)]
blue, white = [0, 0]


def check_color(x, y, size):
    flag = False
    current_color = colors[y][x]
    for i in range(y, y+size):
        for j in range(x, x+size):
            if current_color != colors[i][j]:  # 색이 하나라도 다르면
                flag = True
                break
        if flag:
            break

    if flag:
        next_size = size // 2
        check_color(x, y, next_size)
        check_color(x + next_size, y, next_size)
        check_color(x, y + next_size, next_size)
        check_color(x + next_size, y + next_size, next_size)
    else:
        global blue, white
        if current_color == '1':
            blue += 1
        else:
            white += 1
        return


check_color(0, 0, N)
print(white)
print(blue)