# 1 1 => False

a , b = map(int, input().split())

checkerA = bool(a)
checkerB = bool(b)
checker = checkerA != checkerB
print(checker)