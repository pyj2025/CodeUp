# 0 0 => True

a,b = map(int, input().split())

checkerA = bool(a)
checkerB = bool(b)

checker = not checkerA and not checkerB
print(checker)
