# 트리 순회 - 이진 트리
import sys

level = int(sys.stdin.readline())
tree = []
for _ in range(level):
    tree.append(sys.stdin.readline().split())

## 전위 순회: (루트)(왼쪽 자식)(오른쪽 자식)
pre = ''
def preorder(t):
    global pre
    pre += t[0]
    if t[1]:
        for i in tree:
            if i[0] == t[1]:
                preorder(i)
                break
    if t[2]:
        for i in tree:
            if i[0] == t[2]:
                preorder(i)
                break
preorder(tree[0])
print(pre)

## 중위 순회: (왼쪽 자식) (루트) (오른쪽 자식)
ino = ''
def inorder(t):
    global ino
    if t[1]:
        for i in tree:
            if i[0] == t[1]:
                inorder(i)
                break
    ino += t[0]
    if t[2]:
        for i in tree:
            if i[0] == t[2]:
                inorder(i)
                break
inorder(tree[0])
print(ino)

## 후위 순회: (왼쪽 자식) (오른쪽 자식) (루트)
post = ''
def postorder(t):
    global post
    if t[1]:
        for i in tree:
            if i[0] == t[1]:
                postorder(i)
                break
    if t[2]:
        for i in tree:
            if i[0] == t[2]:
                postorder(i)
                break
    post += t[0]
postorder(tree[0])
print(post)