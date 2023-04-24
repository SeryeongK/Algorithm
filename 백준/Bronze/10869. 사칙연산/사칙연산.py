import math

data = input()
num = data.split()
a = int(num[0])
b = int(num[1])

def add(a, b):
    return print(a + b)

def minus(a, b):
    return print(a - b)

def times(a, b):
    return print(a * b)

def div(a, b):
    return print(math.floor(a / b))

def left(a, b):
    return print(a % b)

add(a, b)
minus(a, b)
times(a, b)
div(a, b)
left(a, b)
