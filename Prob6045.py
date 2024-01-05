# 1 2 3 => 6 2.00

a,b,c = map(int, input().split())

total = a + b + c
average = format(total / 3, ".2f")

print(f'{total} {average}')