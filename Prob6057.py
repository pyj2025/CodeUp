# 0 0 => True

a , b = map(int, input().split())

checkerA = bool(a)
checkerB = bool(b)
checker = checkerA == checkerB
print(checker)