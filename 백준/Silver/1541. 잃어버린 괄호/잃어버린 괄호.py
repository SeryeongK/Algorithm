# 잃어버린 괄호
import sys
input = ['(']+list(sys.stdin.readline().strip())+[')']
for i in range(len(input)):
    if input[i] == '0':
        if input[i-1] == '(' or input[i-1] == '' or input[i-1] == '+' or input[i-1] == '-':
            input[i] = ''
    # print(f"i: {i}, input[i]: {input[i]}, input: {input}")

st = ''.join(input)
print(eval(st.replace('-', ')-(')))