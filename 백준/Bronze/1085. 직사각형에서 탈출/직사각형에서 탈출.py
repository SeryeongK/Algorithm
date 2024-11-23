x, y, w, h = map(int, input().split())

min = x

def changeMin(num):
    global min
    if num < min:
        min = num

changeMin(y)
changeMin(w - x)
changeMin(h - y)
print(min)