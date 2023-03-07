# 알파벳 찾기
import sys

input = sys.stdin.readline().strip()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
output = []

## 🚨 문자열에서 찾기 => find()
for i in range(len(alphabet)):
    output.append(str(input.find(alphabet[i])))

## 🚨 배열의 값을 문자열로 변환할 때 => join
print(" ".join(output))